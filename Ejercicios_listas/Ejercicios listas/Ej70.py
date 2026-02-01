#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.

lista=[]
lista2=[]
repetir="s"
cantidad=int(input("Introduce la cantidad de palabras: "))

for x in range(cantidad):
    letra=input("Introduce una palabra: ")
    if not(letra in lista):
        lista.append(letra)
    if not(letra in lista2):
        lista2.append(letra)
        lista2.sort(reverse=True)
print(lista)
print(lista2)