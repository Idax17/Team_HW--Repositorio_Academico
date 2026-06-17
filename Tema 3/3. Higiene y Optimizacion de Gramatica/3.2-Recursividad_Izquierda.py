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
