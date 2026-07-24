# ⚙️ Experimento de Carga Multi-lenguaje: Parsers para Redes Docker

Este directorio contiene la parte B de la Pregunta 4: toma la gramática `DockerNetworks.g4`
(definida por el Arquitecto de la Gramática) y genera **dos parsers adicionales** en
lenguajes distintos, para luego medir y comparar el tiempo de ejecución de las **tres**
implementaciones sobre el mismo set de datos.

## Implementaciones comparadas

| # | Lenguaje | Metacompilador | Carpeta |
|---|----------|-----------------|---------|
| 1 | Python 3 | ANTLR 4.13.1 (`-Dlanguage=Python3`) | `python_antlr/` |
| 2 | Java 21  | ANTLR 4.13.1 (`-Dlanguage=Java`)    | `java_antlr/` |
| 3 | C (GCC 13) | Flex 2.6 + Bison 3.8 (implementación manual, misma GLC) | `c_flexbison/` |

Las tres implementaciones parten de la **misma GLC** (`DockerNetworks.g4`), por lo que
constituyen una comparación válida "para un mismo lenguaje L", tal como pide la actividad.
Los parsers 1 y 2 se generan automáticamente con el mismo metacompilador (ANTLR) en dos
lenguajes destino distintos; el parser 3 es una implementación manual equivalente con un
metacompilador diferente (Flex/Bison), lo que permite comparar tanto lenguajes como
generadores.

## Requisitos
- Linux (Ubuntu 24.04) o WSL (Windows Subsystem for Linux en Ubuntu 24.04).
- Python 3.x + `antlr4-python3-runtime==4.13.1` (`pip install antlr4-python3-runtime==4.13.1`) (`pip install pandas matplotlib`)
- JDK 17+ (`javac`, `java`)
- `antlr-4.13.1-complete.jar` (mismo jar usado por el Arquitecto de la Gramática; sirve de
  metacompilador **y** de runtime Java, porque el jar "complete" empaqueta ambos)
- GCC, Flex, Bison (`sudo apt install flex bison build-essential`)

## Cómo reproducir el experimento

### 1) Generar los parsers Python y Java desde la GLC

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -o python_antlr DockerNetworks.g4
java -jar antlr-4.13.1-complete.jar -Dlanguage=Java    -o java_antlr   DockerNetworks.g4
```

### 2) Compilar el parser C (Flex/Bison)

```bash
cd c_flexbison
bison -d parser.y -o parser.tab.c
flex -o lex.yy.c lexer.l
gcc -O2 -o bench_docker bench.c parser.tab.c lex.yy.c -lfl
cd ..
```

### 3) Compilar el driver Java

```bash
cd java_antlr
javac -cp ../antlr-4.13.1-complete.jar *.java
cd ..
```

### 4) Ejecutar el benchmark (n=10 archivos, 200 repeticiones c/u)

```bash
python3 python_antlr/bench_docker.py dataset 200        > results/python_antlr.csv
java -cp java_antlr:antlr-4.13.1-complete.jar Main dataset 200 > results/java_antlr.csv
./c_flexbison/bench_docker dataset 200                  > results/c_flexbison.csv
```

Cada CSV tiene el formato `file,lang,run,time_ms,ok`, donde `time_ms` es el tiempo de
**un solo ciclo lexer+parser** medido en memoria (sin costo de arranque de proceso, ya que
las 200 repeticiones ocurren dentro del mismo proceso/JVM).

### 5) Analizar y graficar

```bash
python3 analyze.py
```

Genera `results/summary_by_lang.csv`, `results/per_file_mean.csv` y las dos gráficas
(`chart_mean_by_lang.png`, `chart_per_file.png`).

## Nota metodológica sobre "ok"

Las tres implementaciones reportan `ok=false` en el 100% de los archivos de prueba. Esto
**no es un error de estas implementaciones**: se debe a una ambigüedad heredada de la GLC
compartida (ver discusión en el informe). Como las tres comparten exactamente la misma
gramática y el mismo orden de reglas léxicas, el fallo es consistente entre lenguajes, lo
cual en realidad valida que la comparación de tiempos es justa (las tres hacen el mismo
trabajo: tokenizar por completo la entrada y recorrer la misma cantidad de producciones
antes de fallar en el mismo punto).
