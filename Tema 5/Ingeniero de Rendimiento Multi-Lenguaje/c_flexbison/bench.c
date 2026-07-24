#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <dirent.h>

int yyparse(void);
typedef struct yy_buffer_state *YY_BUFFER_STATE;
YY_BUFFER_STATE yy_scan_string(const char *str);
void yy_delete_buffer(YY_BUFFER_STATE b);
extern int syntax_ok;

static char *read_file(const char *path, long *out_len) {
    FILE *f = fopen(path, "rb");
    if (!f) return NULL;
    fseek(f, 0, SEEK_END);
    long len = ftell(f);
    fseek(f, 0, SEEK_SET);
    char *buf = malloc(len + 1);
    fread(buf, 1, len, f);
    buf[len] = '\0';
    fclose(f);
    if (out_len) *out_len = len;
    return buf;
}

/* simple case-insensitive-free filename comparator for stable ordering */
static int cmp_names(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr, "Uso: %s <dataset_dir> <repeats>\n", argv[0]);
        return 2;
    }
    const char *dir_path = argv[1];
    int repeats = atoi(argv[2]);

    DIR *d = opendir(dir_path);
    if (!d) { fprintf(stderr, "No se pudo abrir directorio\n"); return 2; }

    char *names[256];
    int n = 0;
    struct dirent *ent;
    while ((ent = readdir(d)) != NULL) {
        size_t l = strlen(ent->d_name);
        if (l > 4 && strcmp(ent->d_name + l - 4, ".yml") == 0) {
            names[n] = strdup(ent->d_name);
            n++;
        }
    }
    closedir(d);
    qsort(names, n, sizeof(char *), cmp_names);

    printf("file,lang,run,time_ms,ok\n");

    for (int i = 0; i < n; i++) {
        char full_path[1024];
        snprintf(full_path, sizeof(full_path), "%s/%s", dir_path, names[i]);
        long len;
        char *content = read_file(full_path, &len);
        if (!content) continue;

        for (int r = 0; r < repeats; r++) {
            struct timespec start, end;
            clock_gettime(CLOCK_MONOTONIC, &start);

            syntax_ok = 1;
            YY_BUFFER_STATE buf = yy_scan_string(content);
            yyparse();
            yy_delete_buffer(buf);

            clock_gettime(CLOCK_MONOTONIC, &end);
            double ms = (end.tv_sec - start.tv_sec) * 1000.0 +
                        (end.tv_nsec - start.tv_nsec) / 1e6;
            printf("%s,c_flexbison,%d,%f,%s\n", names[i], r, ms, syntax_ok ? "true" : "false");
        }
        free(content);
    }
    return 0;
}
