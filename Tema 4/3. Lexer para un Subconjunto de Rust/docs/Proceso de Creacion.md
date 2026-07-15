# Proceso de creación del lexer para MiniRust

Este documento registra, paso a paso, cómo se construyó el analizador léxico,
incluyendo las decisiones de diseño y los ajustes realizados durante las pruebas.

## Paso 1 — Selección y acotación del lenguaje L

Se decidió tomar como base el lenguaje Rust por ser un lenguaje moderno con una
sintaxis rica (tipos explícitos, `struct`/`impl`, *pattern matching* con `match`,
anotaciones de mutabilidad con `mut`), lo que permite ejercitar una variedad amplia
de categorías léxicas: palabras reservadas, tipos, operadores compuestos (`->`, `=>`,
`::`), literales de varios tipos y comentarios de línea y de bloque. Se acotó el
subconjunto a las construcciones que pueden reconocerse puramente a nivel léxico
(sin necesidad de análisis sintáctico), documentando explícitamente qué queda fuera
del alcance (ver `01_descripcion_lenguaje_L.md`, sección 5).

## Paso 2 — Catalogación de tokens

Antes de escribir una sola línea de Flex, se elaboró una tabla con cada categoría de
token, un nombre simbólico (`KW_FN`, `TY_INT`, `OP_ARROW`, etc.) y su expresión
regular asociada. Este catálogo es el que después se documentó formalmente en
`01_descripcion_lenguaje_L.md`.

## Paso 3 — Escritura de la especificación `.l`

Se escribió `src/mini_rust.l` siguiendo la estructura estándar de tres secciones de
Flex. Se prestó especial atención a:

- Definir primero las macros reutilizables (`DIGIT`, `LETTER`, `IDENT`, etc.) en la
  sección de definiciones, para no repetir expresiones regulares largas.
- Ordenar las reglas de la sección de reglas siguiendo el criterio: comentarios →
  palabras reservadas → tipos → literales → operadores compuestos → operadores
  simples → puntuación → identificadores → espacios en blanco → error genérico.
  Este orden es crítico en Flex porque, ante coincidencias de igual longitud, se
  aplica la regla que aparece primero.

## Paso 4 — Instalación y generación del analizador

El entorno de trabajo no tenía Flex instalado por defecto, así que se instaló con:

```bash
sudo apt-get install -y flex
```

Luego se generó el código C:

```bash
flex -o lex.yy.c mini_rust.l
```

## Paso 5 — Compilación

```bash
gcc lex.yy.c -o mini_rust_lexer -lfl
```

La primera compilación fue exitosa sin necesidad de ajustes adicionales, gracias a
que la especificación `.l` fue revisada previamente en papel (catálogo de tokens del
Paso 2) antes de traducirla a Flex.

## Paso 6 — Diseño de los casos de prueba

Se diseñaron tres archivos de prueba en `tests/`, cada uno enfocado en un subconjunto
distinto de las reglas del lexer, para tener una cobertura razonable sin necesidad de
un archivo gigantesco:

1. **`ejemplo1_suma.rs`**: funciones, parámetros tipados, `let mut`, operador `->`,
   operador compuesto `+=`, `return`. Verifica el "camino feliz" básico.
2. **`ejemplo2_struct.rs`**: `struct`, `impl`, `self`, condicionales `if/else`,
   `match` con el operador `=>`, literales flotantes, booleanos, de carácter y de
   cadena. Verifica las construcciones más "ricas" del subconjunto.
3. **`ejemplo3_bucles_error.rs`**: los tres tipos de bucle (`while`, `for`, `loop`),
   el operador `::` (usado en `Vec::new()`), y de forma intencional incluye el
   carácter `@` dentro de lo que parecería un identificador (`v@lor`), para
   comprobar que el analizador reporta el error léxico correctamente y **continúa**
   el análisis en lugar de detenerse (tal como se explica en la teoría del Tema 4
   sobre control de errores).

## Paso 7 — Ejecución y verificación de resultados

Cada archivo de prueba se ejecutó así:

```bash
./mini_rust_lexer ../tests/ejemplo1_suma.rs
./mini_rust_lexer ../tests/ejemplo2_struct.rs
./mini_rust_lexer ../tests/ejemplo3_bucles_error.rs
```

Se revisó manualmente la salida de cada uno, confirmando que:

- Las palabras reservadas se clasifican con su token específico y no como `IDENT`.
- Los operadores compuestos (`->`, `+=`, `::`, `==`) se reconocen como una sola
  unidad y no como operadores simples consecutivos.
- Los comentarios de línea y de bloque no generan ningún token.
- El número de línea reportado junto a cada token es correcto.
- El carácter `@` del tercer ejemplo se reporta como **1 error léxico en la línea
  28**, y el análisis continúa reconociendo el resto del archivo (`lor`, `=`, `10`,
  `;`, etc.), en vez de abortar la ejecución.

Las salidas completas de los tres ejemplos quedaron guardadas en
`tests/ejemploN_..._salida.txt` como evidencia.

## Paso 8 — Empaquetado y control de versiones

Finalmente, todo el proyecto (especificación, ejecutable, casos de prueba, salidas y
documentación) se organizó en un repositorio Git local con commits descriptivos por
etapa (especificación inicial, compilación, casos de prueba, documentación), y se
generó un archivo comprimido con el contenido completo del repositorio para su
entrega.
