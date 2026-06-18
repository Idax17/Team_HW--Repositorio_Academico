#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

// Definición de Estados del AFD
enum Estado {
    q0, // Estado Inicial
    q1, // Pieza leída
    q2, // Columna leída
    qf, // Estado de Aceptación (Fila leída)
    qe  // Estado de Error / Trampa
};

// Conversor de enum a string para la visualización de la ejecución
std::string estadoAString(Estado e) {
    switch (e) {
        case q0: return "q0";
        case q1: return "q1";
        case q2: return "q2";
        case qf: return "qf (ACEPTACION)";
        case qe: return "qe (ERROR)";
    }
    return "unknown";
}

// Funciones del alfabeto \Sigma
bool esPieza(char c) { return (c == 'K' || c == 'Q' || c == 'R' || c == 'B' || c == 'N'); }
bool esColumna(char c) { return (c >= 'a' && c <= 'h'); }
bool esFila(char c) { return (c >= '1' && c <= '8'); }

// Función que ejecuta y demuestra el AFD paso a paso
bool ejecutarAutomataPGN(const std::string& cadena) {
    Estado estadoActual = q0;
    std::cout << "\n--------------------------------------------------" << std::endl;
    std::cout << "Evaluando cadena: \"" << cadena << "\"" << std::endl;
    std::cout << "Estado Inicial: " << estadoAString(estadoActual) << std::endl;

    for (size_t i = 0; i < cadena.length(); ++i) {
        char c = cadena[i];
        Estado estadoAnterior = estadoActual;

        // Transiciones del AFD
        switch (estadoActual) {
            case q0:
                if (esPieza(c)) estadoActual = q1;
                else if (esColumna(c)) estadoActual = q2;
                else estadoActual = qe;
                break;
            case q1:
                if (esColumna(c)) estadoActual = q2;
                else estadoActual = qe;
                break;
            case q2:
                if (esFila(c)) estadoActual = qf;
                else estadoActual = qe;
                break;
            case qf:
                // Si hay más caracteres después del estado de aceptación, invalida la estructura básica
                estadoActual = qe;
                break;
            case qe:
                // Permanecer en el estado trampa
                break;
        }

        std::cout << "  Paso " << i + 1 << ": '" << c << "' -> Transicion: " 
                  << estadoAString(estadoAnterior) << " ==> " << estadoAString(estadoActual) << std::endl;

        if (estadoActual == qe) {
            std::cout << "  [Early Exit] Se alcanzo el estado trampa de error." << std::endl;
            return false;
        }
    }

    // Al finalizar la cadena, verificamos si terminamos en el estado de aceptación formal
    bool esAceptado = (estadoActual == qf);
    std::cout << "Resultado Final: " << (esAceptado ? "CADENA ACEPTADA [VALOR VALIDO]" : "CADENA RECHAZADA [SINTAXIS INVALIDA]") << std::endl;
    return esAceptado;
}

int main() {
    // Banco de pruebas con casos límite para validar el comportamiento del autómata
    std::vector<std::string> casosPrueba = {
        "e4",     // Válido: Peón a e4 (q0 -> q2 -> qf)
        "Nf3",    // Válido: Caballo a f3 (q0 -> q1 -> q2 -> qf)
        "Qd8",    // Válido: Dama a d8
        "Bc4",    // Válido: Alfil a c4
        "x3",     // Inválido: Caracter no perteneciente al alfabeto inicial
        "N",      // Inválido: Falta la coordenada destino (Termina en q1, no en qf)
        "e9",     // Inválido: Fila fuera del rango algebraico [1-8]
        "Nf3f",   // Inválido: Caracter extra tras alcanzar la aceptación
        "a1"      // Válido: Límite inferior del tablero
    };

    std::cout << "==========================================================" << std::endl;
    std::cout << "   DEMOSTRACION EN EJECUCION: ANALIZADOR LEXICO/SINTACTICO" << std::endl;
    std::cout << "==========================================================" << std::endl;

    for (const std::string& caso : casosPrueba) {
        ejecutarAutomataPGN(caso);
    }

    return 0;
}