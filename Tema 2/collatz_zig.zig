// Conjetura de Collatz - Implementación en Zig
// Lenguaje y Compiladores 2026-I | UNEG
// Algoritmo: Demostración de la conjetura de Collatz para todo n < 100_000

const std = @import("std");

/// Calcula el número de pasos para que n llegue a 1.
fn collatzPasos(n_inicial: u64) u64 {
    var n = n_inicial;
    var pasos: u64 = 0;
    while (n != 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        pasos += 1;
    }
    return pasos;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const N: u64 = 100_000;

    var timer = try std.time.Timer.start();

    var max_pasos: u64 = 0;
    var numero_max: u64 = 1;
    var i: u64 = 1;

    while (i < N) : (i += 1) {
        const pasos = collatzPasos(i);
        if (pasos > max_pasos) {
            max_pasos = pasos;
            numero_max = i;
        }
    }

    const transcurrido_ns = timer.read();
    const tiempo_ms = @as(f64, @floatFromInt(transcurrido_ns)) / 1_000_000.0;

    try stdout.print("Conjetura de Collatz verificada para todo 1 <= n < {}\n", .{N});
    try stdout.print("Numero con mas pasos: {} ({} pasos)\n", .{ numero_max, max_pasos });
    try stdout.print("Tiempo de ejecucion: {d:.2} ms\n", .{tiempo_ms});
}
