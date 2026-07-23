import difflib
import re

# Definimos las palabras clave permitidas en UnegScript
KEYWORDS = ['var', 'imprimir', 'funcion', 'si', 'sino']

def consultar_llm(tipo_error, contexto, codigo_completo):
    """
    Simula la integración con una API de LLM (como OpenAI, Gemini o DeepSeek).
    Esta es la lógica de conexión para el fallback a la IA.
    """
    print(f"\n[🤖 LLM Conectado] Analizando {tipo_error}...")
    
    # Aquí iría el request real a la API, por ahora simulamos la respuesta inteligente.
    if tipo_error == "Error Léxico":
        return f"IA Sugiere: No reconozco el término '{contexto}'. ¿Intentabas usar una palabra clave como 'imprimir' o declarar una 'var'?"
    elif tipo_error == "Error Sintáctico":
        return f"IA Sugiere: Te falta un símbolo en '{codigo_completo}'. Para declarar variables en UnegScript la estructura es: var [nombre] = [valor]."

def calcular_similitud(palabra, opciones):
    """Implementa el cálculo de similitud usando difflib."""
    # Obtenemos la coincidencia más cercana, si la hay
    coincidencias = difflib.get_close_matches(palabra, opciones, n=1, cutoff=0.0)
    
    if coincidencias:
        mejor_opcion = coincidencias[0]
        # Calculamos el ratio exacto (0.0 a 1.0)
        confianza = difflib.SequenceMatcher(None, palabra, mejor_opcion).ratio()
        return mejor_opcion, confianza
    return None, 0.0

def analizar_lexico(codigo):
    """Lexer con cálculo de umbral de confianza y fallback a IA."""
    tokens = []
    palabras = codigo.split()
    
    print(f"\n--- Analizando Código: '{codigo}' ---")
    
    for palabra in palabras:
        # Si parece una palabra pero no está en las KEYWORDS exactas
        if re.match(r'^[a-zA-Z_]\w*$', palabra) and palabra not in KEYWORDS:
            # 1. Calculamos similitud (Distancia/Difflib)
            mejor_opcion, confianza = calcular_similitud(palabra, KEYWORDS)
            
            # 2. Lógica del umbral
            if confianza >= 0.8 and confianza < 1.0:
                print(f"[!] Autocorrección léxica: '{palabra}' corregido a '{mejor_opcion}' (Confianza: {confianza:.2f})")
                tokens.append(('KEYWORD', mejor_opcion))
            
            # Si es una palabra completamente desconocida y la confianza es < 0.8
            elif confianza < 0.8:
                # Omitimos identificadores válidos (nombres de variables)
                if not palabra.startswith('mi_'): # Regla dummy para el ejemplo
                    print(f"[x] Error Léxico Crítico: '{palabra}'. Confianza: {confianza:.2f} (< 0.8).")
                    
                    # 3. Fallback a la IA
                    respuesta = consultar_llm("Error Léxico", palabra, codigo)
                    print(respuesta)
                    tokens.append(('ERROR', palabra))
                    continue
                else:
                    tokens.append(('IDENTIFICADOR', palabra))
        elif palabra in KEYWORDS:
            tokens.append(('KEYWORD', palabra))
        else:
            tokens.append(('SIMBOLO_O_VALOR', palabra))
            
    return tokens

def analizar_sintaxis(tokens):
    """Parser recursivo descendente básico con fallback a IA."""
    if not tokens or any(t[0] == 'ERROR' for t in tokens):
        return # Detenemos el parser si el lexer falló
        
    print("--- Iniciando Parser ---")
    
    # Simulamos el parseo de una declaración de variable: var IDENTIFICADOR = VALOR
    if tokens[0][0] == 'KEYWORD' and tokens[0][1] == 'var':
        try:
            # Validamos la estructura estricta
            assert tokens[1][0] == 'IDENTIFICADOR'
            assert tokens[2][1] == '='
            print("[✓] Sintaxis correcta: Declaración de variable exitosa.")
        except (IndexError, AssertionError):
            # Fallback a la IA en el Parser
            print("[x] Error Sintáctico detectado en la declaración.")
            codigo_reconstruido = " ".join([t[1] for t in tokens])
            respuesta = consultar_llm("Error Sintáctico", "", codigo_reconstruido)
            print(respuesta)

# ==========================================
# SIMULACIÓN PARA EL VIDEO (PRUEBAS EN VIVO)
# ==========================================
if __name__ == "__main__":
    # Prueba 1: Código perfecto
    tokens = analizar_lexico("var mi_numero = 10")
    analizar_sintaxis(tokens)

    # Prueba 2: Error leve (Autocorrección > 0.8)
    # 'imprimr' se parece mucho a 'imprimir'
    tokens = analizar_lexico("imprimr mi_numero")

    # Prueba 3: Error grave (Fallback IA Lexer < 0.8)
    # 'imprzxt' no se parece a nada
    tokens = analizar_lexico("imprzxt mi_numero")

    # Prueba 4: Error sintáctico (Fallback IA Parser)
    # Falta el símbolo '='
    tokens = analizar_lexico("var mi_numero 10")
    analizar_sintaxis(tokens)