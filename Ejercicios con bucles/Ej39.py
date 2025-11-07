#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.

numeros=int(input("Introduce la cantidad de números que deseas introducir: "))
numero_comprovado=0
total_positivos=0
total_negativos=0
total_0=0
for j in range(numeros):
    numero_comprovado=float(input("introduce un número: "))
    if float(numero_comprovado)>0:
        total_positivos=total_positivos+1
    if float(numero_comprovado)<0:
        total_negativos=total_negativos+1
    if float(numero_comprovado)==0:
        total_0=total_0+1
print("La cantidad de números positivos es:")
print("La cantidad de números negativos es:")
print("La cantidad de números ceros es:",total_0)