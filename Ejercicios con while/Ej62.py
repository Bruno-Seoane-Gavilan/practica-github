#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

concatenar=""
inicio=int(input("Introduce inicio: "))
fin=int(input("Introduce el fin: "))
incremento=int(input("Introduce un incremento: "))
if inicio<fin:
    for x in range(inicio,fin,incremento):
        concatenar=concatenar+str(x)+","
print(concatenar[:-1])