#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
lista=[]
longitud=int(input("Introduce la cantidad de letras que quieres introducir: "))
vocales=['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
for x in range(0,longitud):
    letra=input("Introduce una letra: ")
    if letra not in vocales:
        lista.append(letra)
lista=list(set(lista))
print(lista)
