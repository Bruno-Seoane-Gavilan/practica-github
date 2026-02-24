lista_palabrasecreta=["albahaca","regodeo","oleaginoso","barbilampiño","joyel","orondo","eon","flor","imberbe","acecinar"]
lista_partida=[]
lista_ahorcado=[]
letra=""
repetir=""
import random
palabra_secreta=random.choice(lista_palabrasecreta)
print(palabra_secreta)
for x in palabra_secreta:
    lista_partida.append(str("_"))
print(*lista_partida)
letra=input("")
if letra in palabra_secreta:
    lista_partida=[]
    for x in palabra_secreta:
        if letra==x:
            lista_partida.append(letra)
        else:
            lista_partida.append("_")
else:
    print("La letra no está en la palabra")
print(*lista_partida)
while "_" in lista_partida:
    letra=input("Introduce otra letra: ")
    if letra in palabra_secreta:
        for x in range(len(palabra_secreta)):
            if palabra_secreta[x]==letra:
                lista_partida[x]=letra
    elif letra not in palabra_secreta:
        print("La letra no está en la palabra")
    print(*lista_partida)
print("¡Has ganado!")
