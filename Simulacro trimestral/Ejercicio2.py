suma_positivos=0
suma_negativos=0
contador_cien=0

for x in range(7):
    numero=int(input("Introduce en número: "))
    if numero>0:
        suma_positivos=suma_positivos+numero
        if numero>100:
            contador_cien=contador_cien+1
    else:
        suma_negativos=suma_negativos+numero
print("Suma de positivos:", suma_positivos)
print("Suma de negativos:", suma_negativos)
print("Números mayores de 100: ",contador_cien)
