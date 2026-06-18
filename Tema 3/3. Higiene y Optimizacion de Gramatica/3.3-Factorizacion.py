"""
3.3 — Factorización por la Izquierda
======================================
Gramática de entrada (dangling else):
    S -> if E then S else S
    S -> if E then S

Este script IMPLEMENTA el algoritmo de factorización por la izquierda:
detecta el prefijo común entre las alternativas de un no terminal,
lo extrae, y genera la gramática factorizada equivalente.

Algoritmo general para A -> α β1 | α β2 | ... | γ
(donde α es el prefijo común más largo):

    A  -> α A' | γ
    A' -> β1 | β2 | ...
"""

from collections import defaultdict


def parsear_gramatica(texto):
    gramatica = defaultdict(list)
    for linea in texto.strip().split("\n"):
        linea = linea.strip()
        if not linea or "->" not in linea:
            continue
        izq, der = linea.split("->")
        no_terminal = izq.strip()
        for alt in der.split("|"):
            gramatica[no_terminal].append(alt.strip().split())
    return gramatica


def prefijo_comun_mas_largo(alternativas):
    """Encuentra el prefijo común más largo entre todas las alternativas
    de simbolos (listas de tokens)."""
    if not alternativas:
        return []
    prefijo = alternativas[0]
    for alt in alternativas[1:]:
        nuevo_prefijo = []
        for a, b in zip(prefijo, alt):
            if a == b:
                nuevo_prefijo.append(a)
            else:
                break
        prefijo = nuevo_prefijo
        if not prefijo:
            break
    return prefijo

