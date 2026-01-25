#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
palabra=random.choice(lista)
acertado=False
while not acertado:
    intento=input("Introduce la palabra secreta: ")
    if intento==palabra:
        print("ACERTASTE")
        acertado=True
    else:
        print("SIGUE JUGANDO")