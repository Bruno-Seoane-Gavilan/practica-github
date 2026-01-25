#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. Con listas sin try/except lo más simple posible
numeros=input("Introduce una serie de números separados por comas: ")
lista=numeros.split(",")
for x in lista:
    if '.' in x:
        print("Es un número con decimales")
    else:
        print("No es un número con decimales")
