#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente. Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe algún método que permita sumar el contenido de una lista?
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
total_puntuacion=0
while True:
    palabra=random.choice(lista)
    acertado=False
    intentos=0
    while not acertado:
        veces=input("Introduce la palabra secreta (o 'salir' para terminar): ")
        if veces.lower()=='salir':
            promedio_posible=len(lista)*8/2
            print("Puntuación:", total_puntuacion)
            if total_puntuacion > promedio_posible:
                print("La suerte te acompaña.")
            else:
                print("Mejor no te dediques a los juegos de azar.")
            exit()
        intentos=intentos+1
        if veces==palabra:
            puntos=max(8-intentos+1, 0)
            print("ACERTASTE. Puntos obtenidos en esta partida:", puntos)
            total_puntuacion+=puntos
            acertado=True
        else:
            print("SIGUE JUGANDO")
