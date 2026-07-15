# Manual de usuario — Flex (metacompilador utilizado)

## 1. ¿Qué es Flex y por qué se eligió?

Flex (*Fast Lexical Analyzer Generator*) es una herramienta que recibe un archivo de
especificación (extensión `.l`) donde uno describe, mediante expresiones regulares,
los patrones de cada token de su lenguaje, junto con una acción en C que se ejecuta
cada vez que ese patrón coincide con la entrada. A partir de esa especificación, Flex
genera automáticamente un archivo en C (`lex.yy.c`) que contiene el código completo
del analizador léxico, incluyendo la construcción del autómata finito determinístico
correspondiente. En otras palabras, Flex hace exactamente el trabajo que se explicó
en la parte teórica del Tema 4: convierte un conjunto de expresiones regulares en un
AFD y "codifica" ese autómata por nosotros, en vez de tener que escribirlo a mano.

Se eligió Flex (en lugar de escribir el lexer desde cero en Python, por ejemplo)
porque es la herramienta clásica de metacompilación mencionada en el material de
clase, y porque produce un ejecutable nativo en C, lo cual es más cercano a cómo
funcionan los compiladores reales (el propio front-end de Rust usa un enfoque
conceptualmente similar).

## 2. Estructura de un archivo `.l`

Todo archivo de Flex se divide en tres secciones separadas por la marca `%%`:

```
<definiciones y código C>
%%
<reglas: patrón { acción en C }>
%%
<código C adicional, típicamente main()>
```

- **Sección de definiciones**: aquí van los `#include`, variables globales en C
  (dentro de `%{ ... %}`), opciones de Flex (`%option`) y las macros de expresiones
  regulares reutilizables (por ejemplo `IDENT [a-zA-Z_][a-zA-Z0-9_]*`).
- **Sección de reglas**: cada línea es un patrón (expresión regular) seguido de una
  acción en C entre llaves. Cuando la entrada coincide con un patrón, Flex ejecuta esa
  acción y coloca el texto reconocido en la variable global `yytext`.
- **Sección de código de usuario**: normalmente aquí se define `main()`, que abre el
  archivo de entrada y llama a `yylex()` para iniciar el análisis.

## 3. Opciones utilizadas en este proyecto

- `%option noyywrap`: le indica a Flex que no debe esperar una función `yywrap()`
  para manejar múltiples archivos de entrada; con esta opción, al llegar al final del
  archivo el análisis simplemente termina.
- `%option yylineno`: activa el conteo automático de líneas, disponible en la
  variable `yylineno`. Se usa para que cada token impreso indique en qué línea del
  código fuente apareció, lo cual es muy útil para reportar errores léxicos con
  precisión.

## 4. Variables y funciones clave que provee Flex

| Elemento | Significado |
|---|---|
| `yytext` | Cadena de texto que acaba de coincidir con el patrón actual (el *lexema*). |
| `yylineno` | Número de línea actual del archivo de entrada (requiere `%option yylineno`). |
| `yyin` | Puntero de archivo (`FILE *`) desde donde Flex lee la entrada. Si no se asigna, lee de `stdin`. |
| `yylex()` | Función generada por Flex que ejecuta el ciclo de análisis léxico completo. |

## 5. Flujo de trabajo: de la especificación al ejecutable

```
mini_rust.l  --(flex)-->  lex.yy.c  --(gcc)-->  mini_rust_lexer  --(ejecución)-->  tokens
```

1. **Escribir** la especificación `.l` con las reglas del lenguaje `L`.
2. **Generar** el código C con el comando `flex`.
3. **Compilar** ese código C con `gcc`, enlazando la librería de Flex (`-lfl`).
4. **Ejecutar** el binario resultante sobre un archivo fuente de `L` para obtener la
   lista de tokens reconocidos (o los errores léxicos, si los hay).

## 6. Instalación de Flex

En un sistema Debian/Ubuntu (como el usado en este proyecto):

```bash
sudo apt-get update
sudo apt-get install -y flex
```

Esto instala tanto el binario `flex` como la librería de tiempo de ejecución
(`libfl`), necesaria al enlazar el ejecutable final.

Para verificar la instalación:

```bash
flex --version
```

## 7. Comandos de construcción y ejecución (paso a paso)

Desde la carpeta `src/` del repositorio:

```bash
# 1) Generar el analizador en C a partir de la especificación
flex -o lex.yy.c mini_rust.l

# 2) Compilar el analizador generado
gcc lex.yy.c -o mini_rust_lexer -lfl

# 3) Ejecutar el analizador sobre un archivo de código fuente en MiniRust
./mini_rust_lexer ../tests/ejemplo1_suma.rs
```

Si no se pasa ningún archivo como argumento, el analizador lee desde la entrada
estándar (`stdin`), por lo que también se puede usar así:

```bash
./mini_rust_lexer < ../tests/ejemplo1_suma.rs
```

## 8. Interpretación de la salida

Por cada token reconocido, el programa imprime una línea con el siguiente formato:

```
(NOMBRE_DEL_TOKEN , 'lexema', linea N)
```

Al finalizar, se imprime un resumen por la salida de error estándar (`stderr`) con la
cantidad total de tokens reconocidos y la cantidad de errores léxicos encontrados:

```
--- Resumen ---
Tokens reconocidos : 67
Errores lexicos     : 0
```

Si el analizador encuentra un carácter que no corresponde a ningún patrón definido
en `L` (por ejemplo, `@`, `$` o `~`), lo reporta como error léxico indicando el
carácter exacto y el número de línea donde ocurrió, y continúa el análisis con el
resto del archivo (no se detiene en el primer error), tal como se explicó en la
sección teórica del control de errores del Tema 4.

## 9. Errores comunes al trabajar con Flex (aprendidos durante el desarrollo)

- **Orden de las reglas**: Flex prioriza la coincidencia más larga, pero ante un
  empate en longitud, gana la regla que aparece primero en el archivo. Por eso las
  palabras reservadas (`fn`, `let`, etc.) deben ir *antes* que la regla general de
  identificadores; de lo contrario, `fn` se reconocería como `IDENT` en lugar de
  `KW_FN`.
- **Operadores compuestos antes que los simples**: si la regla de `=` apareciera
  antes que la de `==`, Flex igual reconocería `==` correctamente por la regla de
  coincidencia más larga, pero es una buena práctica y más claro ordenar los
  patrones de mayor a menor longitud.
- **Enlazado con `-lfl`**: al compilar con `gcc`, si se omite `-lfl` se puede
  producir un error de enlazado porque el código generado por Flex depende de
  funciones auxiliares de esa librería (relacionadas con `yywrap`).
