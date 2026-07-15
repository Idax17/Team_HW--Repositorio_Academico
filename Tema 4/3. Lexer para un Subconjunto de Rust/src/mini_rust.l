/* ============================================================
 * mini_rust.l
 * Especificacion lexica (Flex) para el lenguaje L = "MiniRust",
 * un subconjunto del lenguaje de programacion Rust.
 *
 * Universidad Nacional Experimental de Guayana (UNEG)
 * Ingenieria en Informatica - Lenguaje y Compiladores
 * Tema 4 (Analisis Lexico) - Actividad 3
 * ============================================================ */

%{
#include <stdio.h>
#include <stdlib.h>

/* Contadores para el resumen final */
static int total_tokens = 0;
static int total_errores = 0;

/* Imprime un token reconocido junto con su lexema, linea y columna */
void emitir(const char *token, const char *lexema);
%}

%option noyywrap
%option yylineno

/* ---------- Definiciones regulares reutilizables ---------- */
DIGIT       [0-9]
LETTER      [a-zA-Z_]
IDENT       {LETTER}({LETTER}|{DIGIT})*
INTEGER     {DIGIT}({DIGIT}|_)*
FLOAT       {DIGIT}({DIGIT}|_)*\.{DIGIT}({DIGIT}|_)*
STRING      \"([^\"\\\n]|\\.)*\"
CHARLIT     \'([^\'\\\n]|\\.)\'

%%

 /* ---------- Comentarios (se ignoran, no generan token) ---------- */
"//".*                     { /* comentario de linea: se ignora */ }
"/*"([^*]|\*+[^*\/])*\*+\/ { /* comentario de bloque: se ignora */ }

 /* ---------- Palabras reservadas de control y declaracion ---------- */
"fn"        { emitir("KW_FN", yytext); }
"let"       { emitir("KW_LET", yytext); }
"mut"       { emitir("KW_MUT", yytext); }
"if"        { emitir("KW_IF", yytext); }
"else"      { emitir("KW_ELSE", yytext); }
"while"     { emitir("KW_WHILE", yytext); }
"for"       { emitir("KW_FOR", yytext); }
"in"        { emitir("KW_IN", yytext); }
"loop"      { emitir("KW_LOOP", yytext); }
"break"     { emitir("KW_BREAK", yytext); }
"continue"  { emitir("KW_CONTINUE", yytext); }
"return"    { emitir("KW_RETURN", yytext); }
"match"     { emitir("KW_MATCH", yytext); }
"struct"    { emitir("KW_STRUCT", yytext); }
"enum"      { emitir("KW_ENUM", yytext); }
"impl"      { emitir("KW_IMPL", yytext); }
"pub"       { emitir("KW_PUB", yytext); }
"use"       { emitir("KW_USE", yytext); }
"mod"       { emitir("KW_MOD", yytext); }
"const"     { emitir("KW_CONST", yytext); }
"static"    { emitir("KW_STATIC", yytext); }
"self"      { emitir("KW_SELF", yytext); }
"Self"      { emitir("KW_SELFTYPE", yytext); }
"as"        { emitir("KW_AS", yytext); }

 /* ---------- Literales booleanos ---------- */
"true"      { emitir("BOOL_LIT", yytext); }
"false"     { emitir("BOOL_LIT", yytext); }

 /* ---------- Tipos primitivos y de biblioteca del subconjunto ---------- */
"i8"|"i16"|"i32"|"i64"   { emitir("TY_INT", yytext); }
"u8"|"u16"|"u32"|"u64"   { emitir("TY_UINT", yytext); }
"f32"|"f64"              { emitir("TY_FLOAT", yytext); }
"bool"                   { emitir("TY_BOOL", yytext); }
"char"                   { emitir("TY_CHAR", yytext); }
"str"                    { emitir("TY_STR", yytext); }
"String"                 { emitir("TY_STRING", yytext); }
"Vec"                    { emitir("TY_VEC", yytext); }

 /* ---------- Literales numericos y de texto ---------- */
{FLOAT}     { emitir("FLOAT_LIT", yytext); }
{INTEGER}   { emitir("INT_LIT", yytext); }
{STRING}    { emitir("STRING_LIT", yytext); }
{CHARLIT}   { emitir("CHAR_LIT", yytext); }

 /* ---------- Operadores compuestos (deben ir antes que los simples) ---------- */
"=="        { emitir("OP_EQ", yytext); }
"!="        { emitir("OP_NEQ", yytext); }
"<="        { emitir("OP_LE", yytext); }
">="        { emitir("OP_GE", yytext); }
"&&"        { emitir("OP_AND", yytext); }
"||"        { emitir("OP_OR", yytext); }
"->"        { emitir("OP_ARROW", yytext); }
"=>"        { emitir("OP_FATARROW", yytext); }
"::"        { emitir("OP_PATHSEP", yytext); }
"+="        { emitir("OP_PLUSEQ", yytext); }
"-="        { emitir("OP_MINUSEQ", yytext); }
"*="        { emitir("OP_STAREQ", yytext); }
"/="        { emitir("OP_SLASHEQ", yytext); }
"%="        { emitir("OP_PERCENTEQ", yytext); }
"<<"        { emitir("OP_SHL", yytext); }
">>"        { emitir("OP_SHR", yytext); }

 /* ---------- Operadores simples ---------- */
"+"         { emitir("OP_PLUS", yytext); }
"-"         { emitir("OP_MINUS", yytext); }
"*"         { emitir("OP_STAR", yytext); }
"/"         { emitir("OP_SLASH", yytext); }
"%"         { emitir("OP_PERCENT", yytext); }
"="         { emitir("OP_ASSIGN", yytext); }
"<"         { emitir("OP_LT", yytext); }
">"         { emitir("OP_GT", yytext); }
"!"         { emitir("OP_NOT", yytext); }
"&"         { emitir("OP_AMP", yytext); }
"|"         { emitir("OP_PIPE", yytext); }
"^"         { emitir("OP_CARET", yytext); }

 /* ---------- Puntuacion / delimitadores ---------- */
"("         { emitir("LPAREN", yytext); }
")"         { emitir("RPAREN", yytext); }
"{"         { emitir("LBRACE", yytext); }
"}"         { emitir("RBRACE", yytext); }
"["         { emitir("LBRACKET", yytext); }
"]"         { emitir("RBRACKET", yytext); }
";"         { emitir("SEMI", yytext); }
","         { emitir("COMMA", yytext); }
":"         { emitir("COLON", yytext); }
"."         { emitir("DOT", yytext); }

 /* ---------- Identificadores (deben ir despues de palabras reservadas) ---------- */
{IDENT}     { emitir("IDENT", yytext); }

 /* ---------- Espacios en blanco: se ignoran ---------- */
[ \t\r]+    { /* se ignora */ }
\n          { /* se ignora, yylineno la cuenta automaticamente */ }

 /* ---------- Cualquier otro caracter: error lexico ---------- */
.           {
              fprintf(stderr, "ERROR LEXICO: caracter no reconocido '%s' en la linea %d\n", yytext, yylineno);
              total_errores++;
            }

%%

void emitir(const char *token, const char *lexema) {
    printf("(%-14s, '%s', linea %d)\n", token, lexema, yylineno);
    total_tokens++;
}

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *entrada = fopen(argv[1], "r");
        if (!entrada) {
            perror("No se pudo abrir el archivo de entrada");
            return 1;
        }
        yyin = entrada;
    }

    yylex();

    fprintf(stderr, "\n--- Resumen ---\n");
    fprintf(stderr, "Tokens reconocidos : %d\n", total_tokens);
    fprintf(stderr, "Errores lexicos     : %d\n", total_errores);

    return total_errores > 0 ? 1 : 0;
}
