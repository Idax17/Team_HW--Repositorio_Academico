// ejemplo3_bucles_error.rs
// Bucles for/while/loop, uso de Vec y un caracter invalido a proposito (@)
// para demostrar la deteccion de errores lexicos del analizador.

fn contar(limite: u32) {
    let mut i: u32 = 0;
    while i < limite {
        i += 1;
    }

    for n in 0..limite {
        if n % 2 == 0 {
            continue;
        }
    }

    let mut contador = 0;
    loop {
        contador += 1;
        if contador >= 5 {
            break;
        }
    }
}

fn main() {
    let numeros: Vec = Vec::new();
    let v@lor = 10;   // '@' no es un caracter valido en un identificador -> error lexico
    contar(numeros);
}
