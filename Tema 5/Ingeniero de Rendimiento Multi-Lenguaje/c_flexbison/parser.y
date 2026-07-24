%{
#include <stdio.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
extern FILE *yyin;
extern int syntax_ok;

%}

%token NETWORKS_KEY DRIVER_KEY IPAM_KEY CONFIG_KEY SUBNET_KEY
%token COLON DASH ID STRING IP_CIDR

%%

composeFile
    : NETWORKS_KEY COLON networkDefList
    ;

networkDefList
    : networkDef
    | networkDefList networkDef
    ;

networkDef
    : ID COLON propertyList
    ;

propertyList
    : property
    | propertyList property
    ;

property
    : DRIVER_KEY COLON STRING
    | IPAM_KEY COLON ipamDef
    ;

ipamDef
    : CONFIG_KEY COLON dashConfigList
    ;

dashConfigList
    : dashConfig
    | dashConfigList dashConfig
    ;

dashConfig
    : DASH SUBNET_KEY COLON IP_CIDR
    ;

%%

int syntax_ok = 1;

void yyerror(const char *s) {
    syntax_ok = 0;
    /* silent: errors are counted, not printed, to keep benchmark output clean */
}

#ifdef STANDALONE
int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Uso: %s <archivo>\n", argv[0]);
        return 2;
    }
    yyin = fopen(argv[1], "r");
    if (!yyin) {
        fprintf(stderr, "No se pudo abrir %s\n", argv[1]);
        return 2;
    }
    yyparse();
    fclose(yyin);
    printf("%s\n", syntax_ok ? "OK" : "FAIL");
    return 0;
}
#endif
