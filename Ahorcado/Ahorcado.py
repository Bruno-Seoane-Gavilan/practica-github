lista_palabrasecreta=["albahaca","regodeo","oleaginoso","barbilampiño","joyel","orondo","eon","flor","imberbe","acecinar"]
lista_partida=[]
lista_ahorcado=[]
letra=""
repetir=""
lista_ahorcado=["A","H","O","R","C","A","D","O"]
errores=0
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
    print(lista_ahorcado[0])
print(*lista_partida)
while "_" in lista_partida:
    letra=input("Introduce otra letra: ")
    if letra in palabra_secreta:
        for x in range(len(palabra_secreta)):
            if palabra_secreta[x]==letra:
                lista_partida[x]=letra
        if letra not in palabra_secreta:
            errores+=1
            if errores<8:
                if errores==1:
                    print(lista_ahorcado[0]+lista_ahorcado[1])
                elif errores==2:
                    print(lista_ahorcado[0]+lista_ahorcado[1]+lista_ahorcado[2])
                elif errores==3:
                    print(lista_ahorcado[0]+lista_ahorcado[1]+lista_ahorcado[2]+lista_ahorcado[3])
                elif errores==4:
                    print(lista_ahorcado[0]+lista_ahorcado[1]+lista_ahorcado[2]+lista_ahorcado[3]+lista_ahorcado[4])
                elif errores==5:
                    print(lista_ahorcado[0]+lista_ahorcado[1]+lista_ahorcado[2]+lista_ahorcado[3]+lista_ahorcado[4]+lista_ahorcado[5])
                elif errores==6:
                    print(lista_ahorcado[0]+lista_ahorcado[1]+lista_ahorcado[2]+lista_ahorcado[3]+lista_ahorcado[4]+lista_ahorcado[5]+lista_ahorcado[6])
                elif errores==7:
                    print(lista_ahorcado[0]+lista_ahorcado[1]+lista_ahorcado[2]+lista_ahorcado[3]+lista_ahorcado[4]+lista_ahorcado[5]+lista_ahorcado[6]+lista_ahorcado[7])
                elif errores==8:
                    print(lista_ahorcado[0]+lista_ahorcado[1]+lista_ahorcado[2]+lista_ahorcado[3]+lista_ahorcado[4]+lista_ahorcado[5]+lista_ahorcado[6]+lista_ahorcado[7]+lista_ahorcado[8])
            print("¡Has perdido!, la palabra secreta era",palabra_secreta)
        if letra not in palabra_secreta:
                print("La letra no está en la palabra")
    print(*lista_partida)
print("¡Has ganado!")