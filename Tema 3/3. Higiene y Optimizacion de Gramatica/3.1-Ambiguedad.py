"""
3.1 — Ambigüedad
================
Gramática:
    E -> E + E
    E -> E * E
    E -> id

Este script construye explícitamente los DOS árboles de derivación
posibles para la cadena "id + id * id" y demuestra que producen
resultados semánticos distintos -> la gramática es ambigua.

No es un parser genérico: construye a mano los dos árboles válidos
(el generador de árboles real requeriría resolver la ambigüedad,
que es precisamente lo que NO tiene esta gramática).
"""


class Nodo:
    """Nodo de un árbol de derivación."""

    def __init__(self, simbolo, hijos=None):
        self.simbolo = simbolo
        self.hijos = hijos or []

    def imprimir(self, prefijo="", es_ultimo=True):
        conector = "└── " if es_ultimo else "├── "
        print(prefijo + conector + self.simbolo)
        nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
        for i, hijo in enumerate(self.hijos):
            hijo.imprimir(nuevo_prefijo, i == len(self.hijos) - 1)

    def evaluar(self):
        """Evalúa el árbol asumiendo que cada 'id' vale 2."""
        if self.simbolo == "id":
            return 2
        if self.simbolo == "+":
            izq, der = self.hijos
            return izq.evaluar() + der.evaluar()
        if self.simbolo == "*":
            izq, der = self.hijos
            return izq.evaluar() * der.evaluar()
        # Nodo E intermedio: delega al único o triple hijo
        if len(self.hijos) == 1:
            return self.hijos[0].evaluar()
        if len(self.hijos) == 3:
            izq, op, der = self.hijos
            return izq.evaluar() + der.evaluar() if op.simbolo == "+" \
                else izq.evaluar() * der.evaluar()
            
def construir_arbol_1():
    """E -> E + E   con  E(id) + (E -> E * E)   =>  id + (id * id)"""
    id1 = Nodo("E", [Nodo("id")])
    id2 = Nodo("E", [Nodo("id")])
    id3 = Nodo("E", [Nodo("id")])
    op_mult = Nodo("*", [id2, id3])
    e_mult = Nodo("E", [op_mult])
    op_suma = Nodo("+", [id1, e_mult])
    raiz = Nodo("E", [op_suma])
    return raiz


def construir_arbol_2():
    """E -> E * E   con  (E -> E + E) * E   =>  (id + id) * id"""
    id1 = Nodo("E", [Nodo("id")])
    id2 = Nodo("E", [Nodo("id")])
    id3 = Nodo("E", [Nodo("id")])
    op_suma = Nodo("+", [id1, id2])
    e_suma = Nodo("E", [op_suma])
    op_mult = Nodo("*", [e_suma, id3])
    raiz = Nodo("E", [op_mult])
    return raiz


def main():
    cadena = "id + id * id"
    print("=" * 60)
    print(f"Gramática: E -> E + E | E * E | id")
    print(f"Cadena analizada: {cadena}")
    print("=" * 60)

    print("\n--- ÁRBOL 1 (la suma se evalúa primero) ---")
    arbol1 = construir_arbol_1()
    arbol1.imprimir()
    valor1 = arbol1.evaluar()
    print(f"Semántica: id + (id * id)")
    print(f"Valor con id=2: {valor1}")

    print("\n--- ÁRBOL 2 (la multiplicación se evalúa primero) ---")
    arbol2 = construir_arbol_2()
    arbol2.imprimir()
    valor2 = arbol2.evaluar()
    print(f"Semántica: (id + id) * id")
    print(f"Valor con id=2: {valor2}")

    print("\n" + "=" * 60)
    print("CONCLUSIÓN")
    print("=" * 60)
    print(f"Misma cadena, dos árboles válidos según la gramática.")
    print(f"Árbol 1 evalúa a {valor1}  |  Árbol 2 evalúa a {valor2}")
    if valor1 != valor2:
        print(">>> La gramática es AMBIGUA: los resultados difieren.")
    else:
        print(">>> Los resultados coinciden (no demuestra ambigüedad en este caso).")


if __name__ == "__main__":
    main()
