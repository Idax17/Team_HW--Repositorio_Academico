# 🚀 Proyecto de Análisis Sintáctico: Parser de Redes Docker

Este documento detalla los requerimientos y pasos necesarios para ejecutar la fase de generación de datos y compilación del parser, correspondiente a la construcción del asistente y análisis sintáctico.

## 📋 Requisitos Previos

Para ejecutar los scripts y compilar la gramática correctamente, asegúrate de contar con las siguientes herramientas en tu entorno:

*   **Python 3.x**: Necesario para ejecutar el script `generar_datos.py` y los analizadores resultantes.
*   **Java Runtime Environment (JRE)**: Indispensable para ejecutar el metacompilador ANTLR.
*   **ANTLR 4** (`antlr-4.13.1-complete.jar`): El archivo binario de ANTLR utilizado para generar el lexer y parser a partir de la GLC.

## 🏗️ Estructura del Directorio

Antes de ejecutar los comandos, tu carpeta de trabajo debe verse de la siguiente manera:

```text
📂 Proyecto_Compiladores/
├── 📄 generar_datos.py           # Script para automatizar la creación del dataset
├── 📄 DockerNetworks.g4          # Archivo de especificación gramatical (GLC)
└── ☕ antlr-4.13.1-complete.jar  # Metacompilador base
```

## ⚙️ Pasos de Ejecución

### Fase 1: Generación del Set de Datos

El primer paso es construir el banco de pruebas de archivos `docker-compose.yml` que serán evaluados por el analizador.

1. Abre tu consola de comandos (CMD) o terminal en la ruta del proyecto.
2. Ejecuta el script generador con el siguiente comando:
   ```bash
   python generar_datos.py
   ```
3. **Resultado esperado:** Se creará automáticamente un directorio llamado `dataset_docker/` conteniendo 10 archivos de configuración YAML listos para ser procesados.

### Fase 2: Compilación del Parser (Metacompilador)

Una vez que los datos de prueba están listos, debes generar los archivos en Python del Lexer y Parser utilizando la especificación de la gramática.

1. En la misma terminal, asegúrate de tener el archivo `.jar` de ANTLR en la carpeta y ejecuta:
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 DockerNetworks.g4
   ```
2. **Resultado esperado:** ANTLR generará automáticamente los archivos fuente (ej. `DockerNetworksLexer.py`, `DockerNetworksParser.py` y archivos de tokens), los cuales serán importados en la fase de pruebas y medición de tiempos.