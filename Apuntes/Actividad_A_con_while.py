import random
num=random.randint(1,20)
num_introducido=int(input("Introduce el numero que crees que es: "))
cont=2

while not(num_introducido==num) and not(cont==0):
    print("El número no es correcto")
    num_introducido=int(input("Introduce otro número que crees que pueda ser: "))
    cont=cont-1
if cont==0 and not(num==num_introducido):
    print("Ya no tienes intentos")
else:
    print("El número es correcto")