#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo

import math
a=int (input("Introduce el valor de a: "))
b=int (input("Introduce el valor de b: "))
c=int (input("Introduce el valor de c: "))
primera_raíz=b**2-4*a*c
if primera_raíz<0:
    print("La raíz no puede ser un número negativo")
else:
    raiz1=(-b+math.sqrt(primera_raíz))/(2*a)
    raiz2=(-b-math.sqrt(primera_raíz))/(2*a)
    print("El valor de x1 es:", raiz1)
    print("El valor de x2 es:", raiz2)
