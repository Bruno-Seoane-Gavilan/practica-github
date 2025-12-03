#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while

numero=int(input("Introduce un número: "))
multiplicar=1
while not (multiplicar>10):
    numero=numero*multiplicar
    print(round(numero))
    numero=numero/multiplicar
    multiplicar=multiplicar+1