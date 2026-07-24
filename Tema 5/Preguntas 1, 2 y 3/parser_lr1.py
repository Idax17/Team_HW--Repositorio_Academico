# parser_lr1.py

class ParserLRSimulado:
    def __init__(self, lista_tokens):
        self.tokens = lista_tokens + ["$"]
        self.pila_estados = [0]
        self.pila_simbolos = []

    def analizar(self):
        print("[INFO] Iniciando análisis LR(1) ascendente (Shift / Reduce)")
        idx = 0
        while True:
            token = self.tokens[idx]
            estado_actual = self.pila_estados[-1]

            print(f"  Pila Estados: {self.pila_estados} | Símbolos: {self.pila_simbolos} | Token actual: '{token}'")

            if estado_actual == 0 and token == "TK_INT":
                self.pila_simbolos.append(token)
                self.pila_estados.append(1)
                print("  --> [SHIFT] Desplazando 'TK_INT' al Estado 1")
                idx += 1

            elif estado_actual == 1 and token == "TK_PLUS":
                self.pila_simbolos.append(token)
                self.pila_estados.append(2)
                print("  --> [SHIFT] Desplazando 'TK_PLUS' al Estado 2")
                idx += 1

            elif estado_actual == 2 and token == "TK_INT":
                self.pila_simbolos.append(token)
                self.pila_estados.append(3)
                print("  --> [SHIFT] Desplazando 'TK_INT' al Estado 3")
                idx += 1

            elif estado_actual == 3 and token == "$":
                print("  --> [REDUCE] Reduciendo [TK_INT TK_PLUS TK_INT] -> <EXPRESION_SUMA>")
                self.pila_simbolos = ["<EXPRESION_SUMA>"]
                print("\n>> ¡ANÁLISIS EXITOSO! La estructura sintáctica es 100% válida. <<")
                break

            else:
                print(f"  [ERROR SINTÁCTICO] Se esperaba token válido pero se encontró '{token}'")
                raise SyntaxError("Error sintáctico en LR(1)")

if __name__ == "__main__":
    print("=== SCRIPT 3: PARSER ASCENDENTE LR(1) (SHIFT / REDUCE) ===\n")

    # Prueba 1: Éxito
    tokens_validos = ["TK_INT", "TK_PLUS", "TK_INT"]
    print(f"--- Ejecutando Prueba 1 con tokens válidos: {tokens_validos} ---\n")
    parser1 = ParserLRSimulado(tokens_validos)
    try:
        parser1.analizar()
    except SyntaxError:
        pass

    print("\n" + "="*65 + "\n")

    # Prueba 2: Error
    tokens_invalidos = ["TK_INT", "TK_PLUS"]
    print(f"--- Ejecutando Prueba 2 con tokens inválidos: {tokens_invalidos} ---\n")
    parser2 = ParserLRSimulado(tokens_invalidos)
    try:
        parser2.analizar()
    except SyntaxError:
        print("\n>> El Parser contuvo el error de manera controlada como se esperaba. <<")
