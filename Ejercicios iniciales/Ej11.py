#11. Realiza un programa que introduciendo el valor del lado de un cuadrado nos devuelva por pantalla en el área y el perímetro.

lado = float(input("Introduce cuanto mide el lado del cuadrado: "))
area = lado**2
perimetro = 4*lado
area=format(area, ".2f")
perimetro=format(perimetro, ".2f")
print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)
