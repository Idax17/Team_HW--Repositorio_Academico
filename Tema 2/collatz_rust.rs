// Conjetura de Collatz - Implementación en Rust
// Lenguaje y Compiladores 2026-I | UNEG
// Algoritmo: Demostración de la conjetura de Collatz para todo n < 100_000

use std::io::{self, BufRead};
use std::time::Instant;

/// Calcula el número de pasos para que n llegue a 1.
fn collatz_pasos(mut n: u64) -> u64 {
    let mut pasos: u64 = 0;
    while n != 1 {
        if n % 2 == 0 {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        pasos += 1;
    }
    pasos
}

fn main() {
    let n: u64 = 100_000;
    let inicio = Instant::now();

    let mut max_pasos: u64 = 0;
    let mut numero_max: u64 = 1;

    for i in 1..n {
        let pasos = collatz_pasos(i);
        if pasos > max_pasos {
            max_pasos = pasos;
            numero_max = i;
        }
    }

    let transcurrido = inicio.elapsed();
    let tiempo_ms = transcurrido.as_secs_f64() * 1000.0;

    println!("Conjetura de Collatz verificada para todo 1 <= n < {}", n);
    println!("Numero con mas pasos: {} ({} pasos)", numero_max, max_pasos);
    println!("Tiempo de ejecucion: {:.2} ms", tiempo_ms);

    println!("\nPresiona Enter para salir...");
    let stdin = io::stdin();
    let _ = stdin.lock().lines().next();
}