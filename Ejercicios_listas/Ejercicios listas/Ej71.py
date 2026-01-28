#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
lista=[]
longitud=int(input("Introduce la cantidad dde letras que quieres introducir: "))
for x in range(0,longitud):
    letra=input("Introduce una letra: ")
    lista.append(letra)
lista=list(set(lista))
print(lista)