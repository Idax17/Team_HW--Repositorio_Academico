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
            
        elif simbolo == 't':
            # 't': Terminar rama (Restaurar la última posición y ángulo guardados)
            if pila_estados:
                posicion_guardada, angulo_guardado = pila_estados.pop()
                trazador.penup() # Levantar el lápiz para no rayar al regresar
                trazador.goto(posicion_guardada)
                trazador.setheading(angulo_guardado)
                trazador.pendown() # Bajar el lápiz para seguir dibujando
                
        elif simbolo == ' ':
            # Ignorar espacios en blanco por si la cadena los incluye
            continue
        else:
            print(f"Símbolo desconocido omitido: {simbolo}")

    # Mantener la ventana abierta hasta que el usuario haga clic
    pantalla.exitonclick()

# ==========================================
# Zona de Pruebas: Los 5 Ejemplos del Informe
# ==========================================

if __name__ == "__main__":
    # Descomenta el ejemplo que quieras ejecutar y comenta los demás.
    
    # Ejemplo 1: Segmento de recta
    # cadena_objetivo = "a"
    
    # Ejemplo 2: Cuadrado (Giro de 90 grados)
    cadena_objetivo = "a g a g a g a g"
    
    # Ejemplo 3: Rama simple (Avanza, guarda, avanza, y vuelve)
    # cadena_objetivo = "c a t"
    
    # Ejemplo 4: Árbol básico (Con giro de 45 grados para notar la rama)
    # cadena_objetivo = "a c g a t a"
    # dibujar_cadena(cadena_objetivo, longitud_trazo=50, angulo_giro=45) 
    
    # Ejemplo 5: Proyección de cubo (Estructura anidada)
    # cadena_objetivo = "a g a c a g t"

    print(f"Ejecutando la cadena: {cadena_objetivo}")
    
    # Llamada a la función (usa angulo_giro=90 por defecto para el cuadrado)
    dibujar_cadena(cadena_objetivo, longitud_trazo=100, angulo_giro=90)