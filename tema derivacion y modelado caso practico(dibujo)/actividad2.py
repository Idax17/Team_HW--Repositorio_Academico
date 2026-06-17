import turtle

def dibujar_cadena(instrucciones, longitud_trazo=50, angulo_giro=90):
    """
    Interpreta una cadena de la gramática {a, c, g, t} y la dibuja.
    """
    pila_estados = []
    
    # Configuración inicial del lienzo y el trazador
    pantalla = turtle.Screen()
    pantalla.title(f"Dibujando cadena: {instrucciones}")
    
    trazador = turtle.Turtle()
    trazador.pensize(2)
    trazador.speed(3) # Velocidad moderada para ver el paso a paso
    
    # Intérprete de los comandos de la gramática
    for simbolo in instrucciones:
        if simbolo == 'a':
            # 'a': Avanzar dibujando una línea
            trazador.forward(longitud_trazo)
            
        elif simbolo == 'g':
            # 'g': Girar (por defecto 90 grados a la derecha)
            trazador.right(angulo_giro)
            
        elif simbolo == 'c':
            # 'c': Comenzar rama (Guardar posición y ángulo actual en la pila)
            estado_actual = (trazador.position(), trazador.heading())
            pila_estados.append(estado_actual)