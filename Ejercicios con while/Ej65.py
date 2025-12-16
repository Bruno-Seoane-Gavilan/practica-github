#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayor y cuál el menor.

numero=0
mayor=0
menor=0
while not (numero==-99):
    numero = int(input("Introduce un número: "))
    if not (numero==-99):
        if numero>mayor:
            mayor=numero
        if numero<menor or menor==0:
            menor=numero
print("El mayor es: ",mayor)
print("El menor es: ",menor)