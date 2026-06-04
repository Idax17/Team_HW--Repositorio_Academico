/**
 * Conjetura de Collatz - Implementación en JavaScript (Node.js)
 * Lenguaje y Compiladores 2026-I | UNEG
 * Algoritmo: Demostración de la conjetura de Collatz para todo n < 100_000
 */

"use strict";

/**
 * Calcula el número de pasos para que n llegue a 1.
 * @param {number} n - Número inicial
 * @returns {number} Cantidad de pasos
 */
function collatzPasos(n) {
  let pasos = 0;
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
    }
    pasos++;
  }
  return pasos;
}

function main() {
  const N = 100_000;
  const inicio = performance.now();

  let maxPasos = 0;
  let numeroMax = 1;

  for (let i = 1; i < N; i++) {
    const pasos = collatzPasos(i);
    if (pasos > maxPasos) {
      maxPasos = pasos;
      numeroMax = i;
    }
  }

  const fin = performance.now();
  const tiempoMs = (fin - inicio).toFixed(2);

  console.log(`Conjetura de Collatz verificada para todo 1 <= n < ${N}`);
  console.log(`Numero con mas pasos: ${numeroMax} (${maxPasos} pasos)`);
  console.log(`Tiempo de ejecucion: ${tiempoMs} ms`);
}

main();
