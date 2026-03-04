lista_palabrasecreta=["albahaca","escuadra","oleaginoso","babero","fabricar","orondo","eon","flor","imberbe","acecinar"]
lista_partida=[]
lista_ahorcado=["A","H","O","R","C","A","D","O"]
errores=0

import random
palabra_secreta=random.choice(lista_palabrasecreta)
print(palabra_secreta)

for x in palabra_secreta:
    lista_partida.append("_")

print(*lista_partida)

while "_" in lista_partida and errores < 8:
    letra=input("Introduce una letra: ")

    if letra in palabra_secreta:
        for x in range(len(palabra_secreta)):
            if palabra_secreta[x]==letra:
                lista_partida[x]=letra
    else:
        errores += 1
        print("La letra que has introducido no esta en la palabra")
        print("".join(lista_ahorcado[:errores]))

    print(*lista_partida)

if "_" not in lista_partida:
    print("¡Has ganado!")
else:
    print("Has perdido, la palabra secreta era", palabra_secreta)