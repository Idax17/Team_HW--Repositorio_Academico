import re
import sys

# 1. Definición de tokens mediante Expresiones Regulares (Regex)
tokens = [
    # Instrucciones principales de Docker (palabras clave)
    ('FROM', r'\bFROM\b'),
    ('RUN', r'\bRUN\b'),
    ('COPY', r'\bCOPY\b'),
    ('ADD', r'\bADD\b'),
    ('ENV', r'\bENV\b'),
    ('WORKDIR', r'\bWORKDIR\b'),
    ('EXPOSE', r'\bEXPOSE\b'),
    ('CMD', r'\bCMD\b'),
    ('ENTRYPOINT', r'\bENTRYPOINT\b'),
    ('VOLUME', r'\bVOLUME\b'),
    ('USER', r'\bUSER\b'),
    ('ARG', r'\bARG\b'),
    
    # Comentarios (Líneas que empiezan con #)
    ('COMMENT', r'#.*'),
    
    # Cadenas de texto entre comillas (para paths o comandos complejos)
    ('STRING', r'"[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\''),
    
    # Rutas, flags o argumentos genéricos
    ('ARGUMENT', r'[a-zA-Z0-9_\-\./:\+]+'),
    
    # Operadores y delimitadores comunes en Docker
    ('ASSIGN', r'='),
    ('BACKSLASH', r'\\'),          # Continuación de línea
    ('NEWLINE', r'\n'),             # Salto de línea para control de flujo
    ('SKIP', r'[ \t]+'),            # Ignorar espacios y tabulaciones
    
    # Cualquier carácter no reconocido (Control de errores léxicos)
    ('MISMATCH', r'.'),
]

def docker_lexer(input_text):
    # Unimos las regex en un solo patrón usando grupos nombrados (?P<NAME>pattern)
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens)
    line_num = 1
    line_start = 0
    
    for mo in re.finditer(token_regex, input_text):
        kind = mo.lastgroup
        value = mo.group(kind)
        
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            yield kind, '\\n', line_num - 1, mo.start() - line_start
        elif kind == 'SKIP':
            continue  # Ignoramos espacios en blanco
        elif kind == 'MISMATCH':
            # Reportamos el error léxico con línea y columna
            column = mo.start() - line_start
            raise RuntimeError(f"Error léxico: Carácter inesperado {value!r} en la línea {line_num}, columna {column}")
        else:
            column = mo.start() - line_start
            yield kind, value, line_num, column

# Función auxiliar para leer archivos
def cargar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None

if __name__ == "__main__":
    archivo_prueba = 'Dockerfile2'
    text = cargar_archivo(archivo_prueba)
    
    if text is not None:
        print(f"--- Analizando: {archivo_prueba} ---\n")
        try:
            for token in docker_lexer(text):
                print(f"Token: {token[0]:12} | Lexema: {token[1]:20} | Línea: {token[2]:3} | Columna: {token[3]}")
        except RuntimeError as e:
            print(f"\n[ERROR DETECTADO] {e}")
