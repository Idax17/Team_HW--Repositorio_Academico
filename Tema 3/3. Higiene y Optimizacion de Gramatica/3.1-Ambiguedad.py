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
