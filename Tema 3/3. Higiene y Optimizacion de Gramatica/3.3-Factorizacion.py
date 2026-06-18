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

def factorizar_izquierda(no_terminal, alternativas):
    """
    Agrupa las alternativas por su prefijo común más largo y factoriza.
    Devuelve: (gramatica_modificada: dict, hubo_cambio: bool)
    """
    prefijo = prefijo_comun_mas_largo(alternativas)

    if not prefijo:
        # No hay prefijo común entre TODAS; buscamos pares que sí comparten
        # prefijo de longitud >= 1 (caso típico de dangling-else con 2 reglas)
        grupos = defaultdict(list)
        for alt in alternativas:
            clave = alt[0] if alt else "ε"
            grupos[clave].append(alt)

        resultado = {}
        nuevo_contador = 1
        nuevas_alts_A = []
        extra_no_terminales = {}

        for clave, grupo in grupos.items():
            if len(grupo) == 1:
                nuevas_alts_A.append(grupo[0])
                continue
            sub_prefijo = prefijo_comun_mas_largo(grupo)
            sufijos = [alt[len(sub_prefijo):] or ["ε"] for alt in grupo]
            nuevo_nt = f"{no_terminal}'"
            nuevas_alts_A.append(sub_prefijo + [nuevo_nt])
            extra_no_terminales[nuevo_nt] = sufijos

        resultado[no_terminal] = nuevas_alts_A
        resultado.update(extra_no_terminales)
        return resultado, bool(extra_no_terminales)

    # Hay un prefijo común a TODAS las alternativas
    sufijos = [alt[len(prefijo):] or ["ε"] for alt in alternativas]
    nuevo_nt = f"{no_terminal}'"
    resultado = {
        no_terminal: [prefijo + [nuevo_nt]],
        nuevo_nt: sufijos
    }
    return resultado, True


def imprimir_gramatica(gramatica, titulo):
    print(f"\n--- {titulo} ---")
    for nt, alternativas in gramatica.items():
        derecha = "  |  ".join(" ".join(alt) for alt in alternativas)
        print(f"  {nt}  ->  {derecha}")
