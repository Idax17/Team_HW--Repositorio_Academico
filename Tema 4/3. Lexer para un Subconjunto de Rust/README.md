# MiniRust Lexer

Analizador léxico, construido con **Flex**, para **MiniRust**: un subconjunto del
lenguaje de programación **Rust** diseñado como lenguaje `L` para la Actividad 3 del
Tema 4 (Análisis Léxico) — Lenguaje y Compiladores, UNEG.

## Contenido del repositorio

```
rust_lexer/
├── README.md                          <- este archivo
├── src/
│   └── mini_rust.l                    <- especificacion Flex del lexer
├── tests/
│   ├── ejemplo1_suma.rs               <- caso de prueba 1 (codigo fuente MiniRust)
│   ├── ejemplo1_suma_salida.txt       <- salida del lexer para el ejemplo 1
│   ├── ejemplo2_struct.rs             <- caso de prueba 2
│   ├── ejemplo2_struct_salida.txt     <- salida del lexer para el ejemplo 2
│   ├── ejemplo3_bucles_error.rs       <- caso de prueba 3 (incluye error lexico)
│   └── ejemplo3_bucles_error_salida.txt
└── docs/
    ├── Manual Usuario FLEX.md      <- manual de usuario de Flex
    └── Proceso de Creacion.md      <- bitacora paso a paso del desarrollo
```

## Requisitos

- Sistema operativo tipo Linux (probado en Ubuntu 24.04).
- `flex` (generador léxico).
- `gcc` (compilador de C).

## Instalación

```bash
sudo apt-get update
sudo apt-get install -y flex gcc
```

## Compilación del lexer

```bash
cd src
flex -o lex.yy.c mini_rust.l
gcc lex.yy.c -o mini_rust_lexer -lfl
```

## Ejecución

```bash
./mini_rust_lexer ../tests/ejemplo1_suma.rs
./mini_rust_lexer ../tests/ejemplo2_struct.rs
./mini_rust_lexer ../tests/ejemplo3_bucles_error.rs
```

También puede leerse desde entrada estándar:

```bash
./mini_rust_lexer < ../tests/ejemplo1_suma.rs
```

## Documentación

Para el detalle completo del lenguaje `L`, el manual de uso de Flex y el proceso de
construcción, ver los archivos dentro de `docs/`, en el orden numerado.

## Autor

Daniel Valenzuela (SonixCDOWO) — Ingeniería en Informática, UNEG.
Asignatura: Lenguaje y Compiladores, Sección 01 — Msc. Félix Márquez.
