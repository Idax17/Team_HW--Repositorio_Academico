"""
Conjetura de Collatz - Implementación en Python
Lenguaje y Compiladores 2026-I | UNEG
Algoritmo: Demostración de la conjetura de Collatz para todo n < 100_000
"""

import time
import sys


def collatz_pasos(n: int) -> int:
    """Calcula el número de pasos para que n llegue a 1."""
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos


def main():
    N = 100_000
    inicio = time.perf_counter()

    max_pasos = 0
    numero_max = 1

    for i in range(1, N):
        pasos = collatz_pasos(i)
        if pasos > max_pasos:
            max_pasos = pasos
            numero_max = i

    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000.0

    print(f"Conjetura de Collatz verificada para todo 1 <= n < {N}")
    print(f"Numero con mas pasos: {numero_max} ({max_pasos} pasos)")
    print(f"Tiempo de ejecucion: {tiempo_ms:.2f} ms")
    input("\nPresiona Enter para salir...")


if __name__ == "__main__":
    main()
