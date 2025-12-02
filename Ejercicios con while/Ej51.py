#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While

cont=int(input("Introduce cuantas veces quieres que se repita: "))
while not(cont==0):
    print("Buenos días")
    cont=cont-1