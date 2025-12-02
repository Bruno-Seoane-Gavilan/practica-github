#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos

import random
numero=random.randint(0,1000)
numero_introducido=0
intentos=0
intentos=int(input("Introduce cuantos intentos quieres tener: "))
while not (numero==numero_introducido) and not (intentos<=0):
    numero_introducido=int(input("Introduce un número entre 0 y 1000: "))
    if numero_introducido==numero:
        print("Número acertado")
    if numero_introducido>=numero:
        print("Número es más pequeño")
    if numero_introducido<=numero:
        print("Número es más grande")
    intentos=intentos-1
if intentos<=0:
    print("Has perdido, ya no tienes intentos")
else:
    print("Acertaste, te quedaban",intentos,"intentos")