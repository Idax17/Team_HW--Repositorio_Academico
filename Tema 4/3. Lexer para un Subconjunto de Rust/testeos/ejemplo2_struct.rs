/* ejemplo2_struct.rs
   Uso de struct, impl, condicionales y match */

struct Punto {
    x: f64,
    y: f64,
}

impl Punto {
    fn distancia_origen(self) -> f64 {
        if self.x == 0.0 && self.y == 0.0 {
            return 0.0;
        } else {
            return self.x * self.x + self.y * self.y;
        }
    }
}

fn clasificar(n: i32) -> str {
    match n {
        0 => "cero",
        _ => "otro",
    }
}

fn main() {
    let p: Punto = Punto { x: 3.5, y: 4.5 };
    let d = p.distancia_origen();
    let activo: bool = true;
    let etiqueta = 'A';
    let nombre: String = "MiniRust";
}
