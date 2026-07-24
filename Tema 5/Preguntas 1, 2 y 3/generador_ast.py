# generador_ast.py

class NodoAST:
    def __init__(self, tipo_token, valor, izquierdo=None, derecho=None):
        self.tipo_token = tipo_token  # Ej: 'OPERADOR', 'NUMERO', 'VARIABLE'
        self.valor = valor            # Ej: '+', '*', '3', 'x'
        self.izquierdo = izquierdo    # Hijo izquierdo
        self.derecho = derecho        # Hijo derecho

    def mostrar(self, nivel=0):
        # Método para dibujar el árbol de forma jerárquica en la terminal
        resultado = "    " * nivel + f"└── [{self.tipo_token}: {self.valor}]\n"
        if self.izquierdo:
            resultado += self.izquierdo.mostrar(nivel + 1)
        if self.derecho:
            resultado += self.derecho.mostrar(nivel + 1)
        return resultado

if __name__ == "__main__":
    print("=== SCRIPT 1: GENERADOR DE ÁRBOL DE SINTAXIS ABSTRACTA (AST) ===")
    print("Simulando la estructura para la expresión: 3 + 5 * 2\n")

    # 1. Construimos las hojas (los números)
    num3 = NodoAST("NUMERO", "3")
    num5 = NodoAST("NUMERO", "5")
    num2 = NodoAST("NUMERO", "2")

    # 2. La multiplicación tiene mayor prioridad, va más abajo en el árbol
    nodo_multiplicacion = NodoAST("OPERADOR", "*", num5, num2)

    # 3. La suma es la raíz que une el 3 con el resultado de la multiplicación
    raiz_arbol = NodoAST("OPERADOR", "+", num3, nodo_multiplicacion)

    # 4. Imprimimos el resultado estructural
    print("Estructura jerárquica del AST generada:")
    print(raiz_arbol.mostrar())
