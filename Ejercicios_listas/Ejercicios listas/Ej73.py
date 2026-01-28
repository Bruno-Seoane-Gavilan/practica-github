#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2  (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no 
lista1=["casa", "mesa", "sal", "sol", "agua"]
lista2=["casa", "luz", "tres", "tren", "sol", "pan"]
palabras=[]
no_repetidas=[]

for palabra in lista1:
    if palabra in lista2:
        palabras.append(palabra)
    else:
        no_repetidas.append(palabra)
print("Palabras repetidas:", palabras)
print("Palabras no repetidas:", no_repetidas)