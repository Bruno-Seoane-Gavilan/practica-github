suma_positivos=0
suma_negativos=0
suma_cien=0
contador=0

for x in range(7):
    numero=int(input("Introduce un número: "))
    if numero>0:
        suma_positivos=suma_positivos+numero
    if numero<0:
        suma_negativos=suma_negativos+numero
    if numero>100:
        contador=contador+1
print("Suma positivos: ",suma_positivos)
print("Suma negativos: ",suma_negativos)
print("Mayores de 100: ",contador)