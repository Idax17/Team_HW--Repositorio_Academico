Casos de Estudio y Derivaciones Evaluadas
El intérprete valida y modela dinámicamente los 5 ejemplos paso a paso propuestos por la actividad:
Caso 1: Segmento de recta ("a")
    - Derivación: Derivación: S → D → T → a
    - Resultado: Trazado lineal básico continuo.

Caso 2: Cuadrado Regular ("a g a g a g a g")
    - Derivación: Concatenación recursiva por la derecha de cuatro pares de instrucciones simples de avance y rotación ortogonal.
    - Resultado: Polígono cerrado de 4 aristas perfectas (configurando angulo_giro=90).

Caso 3: Estructura de Retorno Vacío ("c a t")
    - Derivación: S → D → T → c
    D
    t → c
    T
    t → c
    a
    t
    - Resultado: La tortuga guarda su origen, avanza trazando y regresa instantáneamente de forma invisible al punto de partida, demostrando el comportamiento de la Pila.