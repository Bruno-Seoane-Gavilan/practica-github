lista_palabrasecreta=["albahaca","regodeo","oleaginoso","barbilampiño","joyel","orondo","eon","flor","imberbe","acecinar"]
lista_partida=[]
lista_ahorcado=[]
letra=""
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
print(*lista_partida)
