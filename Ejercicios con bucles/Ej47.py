#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida

numero_1=int(input("Introduce el primer número: "))
numero_2=int(input("Introduce el segundo número: "))

if numero_1 < numero_2:
    numeros=list(range(numero_1, numero_2 + 1))
else:
    numeros=list(range(numero_1, numero_2 - 1, -1))

print("-".join(map(str, numeros)))
#.join: para unir diferentes valores