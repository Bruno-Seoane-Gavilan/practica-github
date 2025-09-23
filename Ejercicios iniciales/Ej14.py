#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.

import math

diametro = float(input("Introduce el diámetro del círculo: "))
radio = diametro / 2
area = math.pi * radio**2
perimetro = math.pi * diametro
area = format(area, ".1f")
perimetro = format(perimetro, ".1f")
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)