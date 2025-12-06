#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random
numero=random.randint(1,5)
numero_introducido=0
while not (numero==numero_introducido):
    numero_introducido=int(input("Introduce un número entre 1 y 5: "))
    if numero_introducido==numero:
        print("Número acertado")
    else:
        print("Número no acertado")
