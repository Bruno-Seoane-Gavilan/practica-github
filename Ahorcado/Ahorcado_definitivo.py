lista_palabrasecreta=["albahaca","escuadra","oleaginoso","babero","fabricar","orondo","eon","flor","imberbe","acecinar"]
lista_partida=[]
lista_ahorcado=["A","H","O","R","C","A","D","O"]
errores=0
repetir="s"
lista_aciertos=[]
lista_errores=[]
num_errores=0
num_aciertos=0
redondear_tiempo=0
cronometro="s"

import datetime
import random
import time

def guardar_partida(palabra, aciertos, errores):
    fecha_hora=datetime.datetime.now()
    fecha=fecha_hora.strftime("%d/%m/%Y")
    hora=fecha_hora.strftime("%H:%M:%S")

    with open("historial_ahorcado.txt","a") as archivo:
        archivo.write("Fecha: "+fecha+
                      " | Hora: "+hora+
                      " | Palabra: "+palabra+
                      " | Aciertos: "+str(aciertos)+
                      " | Errores: "+str(errores)+"\n")

cronometro=input("¿Quieres activar el cronómetro? (si/no): ")
while cronometro in ["si","sí", "s", "S", "Si", "SI"]:

    while repetir in ["si","sí", "s", "S", "Si", "SI"]:
        lista_aciertos=[]
        lista_errores=[]
        lista_partida=[]
        errores=0
        num_errores=0
        num_aciertos=0

        palabra_secreta=random.choice(lista_palabrasecreta)
        lista_palabrasecreta.remove(palabra_secreta)

        for x in palabra_secreta:
            lista_partida.append("_")
        print(*lista_partida)
        tiempo_inicio=time.time()

        while "_" in lista_partida and errores<8:
            letra=input("Introduce una letra: ")
            if not letra.isalpha() or not(len(letra)==1):
                print("Introduce solo una letra")
                continue
            if letra in lista_aciertos or letra in lista_errores:
                print("Ya has usado esa letra")
                continue
            if letra in palabra_secreta:
                for x in range(len(palabra_secreta)):
                    if palabra_secreta[x]==letra:
                        lista_partida[x]=letra
                lista_aciertos.append(letra)
                num_aciertos=len(lista_aciertos)
            else:
                print("La letra que has introducido no esta en la palabra")
                errores=errores+1
                print("".join(lista_ahorcado[:errores]))
                lista_errores.append(letra)
                num_errores=len(lista_errores)
                print("Letras no acertadas:", lista_errores)
            print(*lista_partida)
            if "_" not in lista_partida:
                tiempo_final=time.time()
                tiempo_total=tiempo_final-tiempo_inicio
                redondear_tiempo=round(tiempo_total,3)
                print("¡Has ganado!")
                print("Has acertado",num_aciertos,"letras")
                print("Has fallado",num_errores,"veces")
                print("Has tardado",redondear_tiempo,"segundos en adivinar la palabra")
                guardar_partida(palabra_secreta,num_aciertos,num_errores)
                nuevas_palabras=input("¿Quieres añadir nuevas palabras al juego? (si/no): ")
                if nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                    while nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                        nueva_palabra=input("Introduce la nueva palabra: ")
                        lista_palabrasecreta.append(nueva_palabra)
                        nuevas_palabras=input("¿Quieres añadir otra palabra? (si/no): ")
                repetir=input("¿Quieres jugar otra vez? (si/no): ")
                if repetir not in ["si","sí", "s", "S", "Si", "SI"]:
                    print("¡Hasta la próxima!")
        if errores==8:
            print("Has perdido, la palabra secreta era",palabra_secreta)
            guardar_partida(palabra_secreta,num_aciertos,num_errores)
            nuevas_palabras=input("¿Quieres añadir nuevas palabras al juego? (si/no): ")
            if nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                while nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                    nueva_palabra=input("Introduce la nueva palabra: ")
                    lista_palabrasecreta.append(nueva_palabra)
                    nuevas_palabras=input("¿Quieres añadir otra palabra? (si/no): ")
                repetir=input("¿Quieres jugar otra vez? (si/no): ")
            repetir=input("¿Quieres jugar otra vez? (si/no): ")
            if repetir not in ["si","sí", "s", "S", "Si", "SI"]:
                print("¡Hasta la próxima!")


while cronometro in ["no","n","N","No","NO"]:
    while repetir in ["si","sí", "s", "S", "Si", "SI"]:
        lista_aciertos=[]
        lista_errores=[]
        lista_partida=[]
        errores=0
        num_errores=0
        num_aciertos=0

        palabra_secreta=random.choice(lista_palabrasecreta)
        lista_palabrasecreta.remove(palabra_secreta)

        for x in palabra_secreta:
            lista_partida.append("_")
        print(*lista_partida)

        while "_" in lista_partida and errores<8:
            letra=input("Introduce una letra: ")
            if letra in lista_aciertos or letra in lista_errores:
                print("Ya has usado esa letra")
                continue
            if letra in palabra_secreta:
                for x in range(len(palabra_secreta)):
                    if palabra_secreta[x]==letra:
                        lista_partida[x]=letra
                lista_aciertos.append(letra)
                num_aciertos=len(lista_aciertos)
            else:
                print("La letra que has introducido no esta en la palabra")
                errores=errores+1
                print("".join(lista_ahorcado[:errores]))
                lista_errores.append(letra)
                num_errores=len(lista_errores)
                print("Letras no acertadas:", lista_errores)
            print(*lista_partida)
            if "_" not in lista_partida:
                print("¡Has ganado!")
                print("Has acertado",num_aciertos,"letras")
                print("Has fallado",num_errores,"veces")
                guardar_partida(palabra_secreta,num_aciertos,num_errores)
                nuevas_palabras=input("¿Quieres añadir nuevas palabras al juego? (si/no): ")
                if nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                    while nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                        nueva_palabra=input("Introduce la nueva palabra: ")
                        lista_palabrasecreta.append(nueva_palabra)
                        nuevas_palabras=input("¿Quieres añadir otra palabra? (si/no): ")
                repetir=input("¿Quieres jugar otra vez? (si/no): ")
                if repetir not in ["si","sí", "s", "S", "Si", "SI"]:
                    print("¡Hasta la próxima!")
        if errores==8:
            print("Has perdido, la palabra secreta era",palabra_secreta)
            guardar_partida(palabra_secreta,num_aciertos,num_errores)
            nuevas_palabras=input("¿Quieres añadir nuevas palabras al juego? (si/no): ")
            if nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                while nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                    nueva_palabra=input("Introduce la nueva palabra: ")
                    lista_palabrasecreta.append(nueva_palabra)
                    nuevas_palabras=input("¿Quieres añadir otra palabra? (si/no): ")
                repetir=input("¿Quieres jugar otra vez? (si/no): ")
            print("¡Has perdido!, la palabra secreta era",palabra_secreta)
            repetir=input("¿Quieres jugar otra vez? (si/no): ")
            if repetir not in ["si","sí", "s", "S", "Si", "SI"]:
                print("¡Hasta la próxima!") 

