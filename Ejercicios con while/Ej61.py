#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.

numero=int(input("Introduce un número: "))
multiplicar=1
while not (multiplicar>10) and not (numero*multiplicar>=40):
    numero=numero*multiplicar
    print(round(numero))
    numero=numero/multiplicar
    multiplicar=multiplicar+1
print(round(numero*multiplicar))
print("Fin del programa")