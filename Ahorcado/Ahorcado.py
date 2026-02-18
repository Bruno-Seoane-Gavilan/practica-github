lista_palabrasecreta=["uebos","regodeo","oleaginoso","ñuzco","joyel","vagido","gaznapiro","haiga","ful","acecinar"]
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
    for x in palabra_secreta:
        if letra==x:
            lista_partida.append(letra)
print(*lista_partida)