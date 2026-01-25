#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas. 

lista1=["casa", "mesa", "sal", "sol", "agua"]
lista2=["casa", "luz", "tres", "tren", "sol", "pan"]

repetidas=[]
no_repetidas=[]

for palabra in lista1:
    if palabra in lista2:
        repetidas.append(palabra)
    else:
        no_repetidas.append(palabra)
for palabra in lista2:
    if palabra not in lista1:
        no_repetidas.append(palabra)

print("Palabras repetidas:", repetidas)
print("Palabras no repetidas:", no_repetidas)