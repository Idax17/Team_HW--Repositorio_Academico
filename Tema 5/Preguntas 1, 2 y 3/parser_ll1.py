# parser_ll1.py

class ParserLL1Manual:
    def __init__(self, lista_tokens):
        self.tokens = lista_tokens
        self.indice = 0

    def obtener_token_actual(self):
        if self.indice < len(self.tokens):
            return self.tokens[self.indice]
        return "EOF"

    def emparejar(self, token_esperado):
        token_actual = self.obtener_token_actual()
        if token_actual == token_esperado:
            print(f"  [OK] Token emparejado correctamente: {token_esperado}")
            self.indice += 1
        else:
            print(f"  [ERROR SINTÁCTICO] Se esperaba '{token_esperado}' pero se encontró '{token_actual}'")
            raise SyntaxError("Error sintáctico en LL(1)")

    def analizar(self):
        print("[INFO] Iniciando análisis de la regla: NUMERO + NUMERO")
        self.emparejar("TK_INT")
        self.emparejar("TK_PLUS")
        self.emparejar("TK_INT")
        
        if self.obtener_token_actual() == "EOF":
            print("\n>> ¡ANÁLISIS EXITOSO! La estructura sintáctica es 100% válida. <<")
        else:
            raise SyntaxError("Tokens residuales al final del archivo.")

if __name__ == "__main__":
    print("=== SCRIPT 2: MICRO-PARSER RECURSIVO DESCENDENTE LL(1) ===\n")

    # Prueba 1: Éxito
    tokens_validos = ["TK_INT", "TK_PLUS", "TK_INT"]
    print(f"--- Ejecutando Prueba 1 con tokens válidos: {tokens_validos} ---\n")
    parser1 = ParserLL1Manual(tokens_validos)
    try:
        parser1.analizar()
    except SyntaxError:
        pass

    print("\n" + "="*65 + "\n")

    # Prueba 2: Error
    tokens_invalidos = ["TK_INT", "TK_PLUS"]
    print(f"--- Ejecutando Prueba 2 con tokens inválidos: {tokens_invalidos} ---\n")
    parser2 = ParserLL1Manual(tokens_invalidos)
    try:
        parser2.analizar()
    except SyntaxError:
        print("\n>> El Parser contuvo el error de manera controlada como se esperaba. <<")
