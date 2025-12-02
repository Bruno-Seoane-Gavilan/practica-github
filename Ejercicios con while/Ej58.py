#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random
numero=random.randint(1,5)
numero_introducido=0
vidas=3
while not (numero==numero_introducido) and not(vidas==0):
    numero_introducido=int(input("Introduce un número entre 1 y 5: "))
    if numero_introducido==numero:
        print("Número acertado")
    else:
        print("Número no acertado")
    vidas=vidas-1
