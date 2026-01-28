#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
palabra=random.choice(lista)
letras=list(palabra)
random.shuffle(letras)
palabra_desordenada=''.join(letras)
print("Palabra desordenada:", palabra_desordenada)
intentos=0
while intentos<3:
    intento=input("Adivina la palabra: ")
    intentos+=1
    if intento==palabra:
        print("¡Correcto! Has adivinado la palabra.")
        break
    else:
        print("Incorrecto. Inténtalo de nuevo.")
else:
    print("Lo siento, has agotado tus intentos. La palabra era:", palabra)