// ejemplo1_suma.rs
// Funcion simple que suma dos enteros y retorna el resultado

fn suma(a: i32, b: i32) -> i32 {
    let mut resultado: i32 = a + b;
    resultado += 1;
    return resultado;
}

fn main() {
    let x: i32 = 10;
    let y: i32 = 20;
    let total = suma(x, y);
    println_valor(total);
}
