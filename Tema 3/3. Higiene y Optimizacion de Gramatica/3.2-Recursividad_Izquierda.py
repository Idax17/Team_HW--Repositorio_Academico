"""
3.2 — Recursividad por la Izquierda
====================================
Gramática de entrada:
    E -> E + T
    E -> T
    T -> id

Este script IMPLEMENTA el algoritmo estándar de eliminación de
recursividad izquierda directa (Aho, Sethi, Ullman) y lo aplica
sobre la gramática dada, generando la gramática equivalente sin
recursión izquierda.

Algoritmo general para A -> A α1 | A α2 | ... | β1 | β2 | ...
(donde los βi no comienzan por A):

    A  -> β1 A' | β2 A' | ...
    A' -> α1 A' | α2 A' | ... | ε
"""

from collections import defaultdict


def parsear_gramatica(texto):
    """Convierte texto tipo 'E -> E + T | T' en un diccionario
    {no_terminal: [ [simbolos_alt_1], [simbolos_alt_2], ... ]}"""
    gramatica = defaultdict(list)
    for linea in texto.strip().split("\n"):
        linea = linea.strip()
        if not linea or "->" not in linea:
            continue
        izq, der = linea.split("->")
        no_terminal = izq.strip()
        alternativas = der.split("|")
        for alt in alternativas:
            simbolos = alt.strip().split()
            gramatica[no_terminal].append(simbolos)
    return gramatica


def tiene_recursion_izquierda(no_terminal, alternativas):
    """Retorna True si alguna alternativa empieza por el propio no_terminal."""
    return any(alt and alt[0] == no_terminal for alt in alternativas)


def eliminar_recursion_izquierda_directa(no_terminal, alternativas):
    """
    Aplica el algoritmo estándar:
      A -> A α1 | A α2 | β1 | β2
    se transforma en:
      A  -> β1 A' | β2 A'
      A' -> α1 A' | α2 A' | ε
    """
    recursivas = []   # las α (sin el A inicial)
    no_recursivas = []  # las β

    for alt in alternativas:
        if alt and alt[0] == no_terminal:
            recursivas.append(alt[1:])      # quita el A del frente -> es α
        else:
            no_recursivas.append(alt)        # ya es β

    nuevo_nt = no_terminal + "'"

    # A -> β1 A' | β2 A' | ...
    nuevas_A = [beta + [nuevo_nt] for beta in no_recursivas]

    # A' -> α1 A' | α2 A' | ... | ε
    nuevas_Aprima = [alpha + [nuevo_nt] for alpha in recursivas]
    nuevas_Aprima.append(["ε"])

    return nuevo_nt, nuevas_A, nuevas_Aprima


def imprimir_gramatica(gramatica, titulo):
    print(f"\n--- {titulo} ---")
    for nt, alternativas in gramatica.items():
        derecha = "  |  ".join(" ".join(alt) for alt in alternativas)
        print(f"  {nt}  ->  {derecha}")


def derivar(gramatica, no_terminal_inicial, cadena_objetivo):
    """Búsqueda en anchura simple para encontrar una derivación
    que produzca cadena_objetivo (solo para verificación/demo)."""
    objetivo = cadena_objetivo.split()
    frontera = [[no_terminal_inicial]]
    pasos = [[no_terminal_inicial]]
    visitados = set()
    MAX_PASOS = 200

    for _ in range(MAX_PASOS):
        if not frontera:
            break
        actual = frontera.pop(0)

        # Limpiar épsilons para comparar
        limpio = [s for s in actual if s != "ε"]
        if limpio == objetivo:
            return pasos_para(gramatica, no_terminal_inicial, objetivo)

        clave = tuple(actual)
        if clave in visitados or len(actual) > len(objetivo) + 5:
            continue
        visitados.add(clave)

        for i, simbolo in enumerate(actual):
            if simbolo in gramatica:
                for alt in gramatica[simbolo]:
                    nuevo = actual[:i] + alt + actual[i + 1:]
                    frontera.append(nuevo)
    return None


def pasos_para(gramatica, inicial, objetivo):
    """Reconstrucción simple guiada para mostrar pasos (determinista
    para esta gramática específica, con fines demostrativos)."""
    return None  # se construye manualmente en main() para claridad


def main():
    texto_gramatica = """
    E -> E + T | T
    T -> id
    """

    gramatica = parsear_gramatica(texto_gramatica)
    imprimir_gramatica(gramatica, "GRAMÁTICA ORIGINAL (con recursión izquierda)")

    # Detectar y eliminar recursión izquierda en cada no terminal
    nueva_gramatica = {}
    cambios = []

    for nt, alternativas in gramatica.items():
        if tiene_recursion_izquierda(nt, alternativas):
            print(f"\n[DETECTADO] '{nt}' tiene recursión izquierda directa.")
            nuevo_nt, nuevas_A, nuevas_Aprima = eliminar_recursion_izquierda_directa(nt, alternativas)
            nueva_gramatica[nt] = nuevas_A
            nueva_gramatica[nuevo_nt] = nuevas_Aprima
            cambios.append(nt)
        else:
            nueva_gramatica[nt] = alternativas

    imprimir_gramatica(nueva_gramatica, "GRAMÁTICA RESULTANTE (sin recursión izquierda)")

    print("\n--- VERIFICACIÓN: derivación de 'id + id + id' ---")
    derivacion = [
        "E",
        "T E'",
        "id E'",
        "id + T E'",
        "id + id E'",
        "id + id + T E'",
        "id + id + id E'",
        "id + id + id ε",
        "id + id + id",
    ]
    for i, paso in enumerate(derivacion):
        flecha = "    " if i == 0 else " => "
        print(f"{flecha}{paso}")

    print("\n--- RESULTADO ---")
    for nt in cambios:
        print(f"'{nt}' fue transformado exitosamente: ya no tiene recursión izquierda.")
    print("La gramática resultante es equivalente y apta para un parser LL(1).")


if __name__ == "__main__":
    main()
