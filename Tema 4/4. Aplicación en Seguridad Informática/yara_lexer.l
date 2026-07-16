%{
#include <stdio.h>
%}

%option noyywrap

%%

"rule"                  { printf("TOKEN: RULE, Lexema: %s\n", yytext); }
"strings:"              { printf("TOKEN: STRINGS_SEC, Lexema: %s\n", yytext); }
"condition:"            { printf("TOKEN: CONDITION_SEC, Lexema: %s\n", yytext); }
"or"                    { printf("TOKEN: OP_OR, Lexema: %s\n", yytext); }
"and"                   { printf("TOKEN: OP_AND, Lexema: %s\n", yytext); }

$[a-zA-Z0-9_]+          { printf("TOKEN: STRING_VAR, Lexema: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("TOKEN: IDENTIFICADOR, Lexema: %s\n", yytext); }
\"[^\"]*\"              { printf("TOKEN: TEXT_STRING, Lexema: %s\n", yytext); }
\{[a-fA-F0-9 \?]+\}     { printf("TOKEN: HEX_STRING, Lexema: %s\n", yytext); }

"="                     { printf("TOKEN: ASIGNACION, Lexema: %s\n", yytext); }
"{"                     { printf("TOKEN: LBRACE, Lexema: %s\n", yytext); }
"}"                     { printf("TOKEN: RBRACE, Lexema: %s\n", yytext); }

\n                      { /* Ignorar nuevas líneas */ }
[ \t]+                  { /* Ignorar espacios y tabulaciones */ }
\/\/.* { /* Ignorar comentarios */ }
.                       { printf("ERROR LÉXICO: Carácter no reconocido: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("Error al abrir el archivo");
            return 1;
        }
        yyin = file;
    }
    yylex();
    return 0;
}