lista_palabrasecreta=["albahaca","escuadra","oleaginoso","babero","fabricar","orondo","eon","flor","imberbe","acecinar"]
lista_partida=[]
lista_ahorcado=["A","H","O","R","C","A","D","O"]
errores=0
repetir="s"
lista_aciertos=[]
lista_errores=[]
lista_letrarepetida=[]
num_errores=0
num_aciertos=0
redondear_tiempo=0
cronometro="s"

import random
cronometro=input("¿Quieres activar el cronómetro? (si/no): ")
while cronometro in ["si","sí", "s", "S", "Si", "SI"]:
    while repetir in ["si","sí", "s", "S", "Si", "SI"]:
        import time
        tiempo_inicio=time.time()
        palabra_secreta=random.choice(lista_palabrasecreta)
        tiempo_final=time.time()
        tiempo_total=tiempo_final-tiempo_inicio
        redondear_tiempo=round(tiempo_total,3)
        palabra_secreta=random.choice(lista_palabrasecreta)
        print(palabra_secreta)
        lista_palabrasecreta.remove(palabra_secreta)

        for x in palabra_secreta:
            lista_partida.append("_")
        print(*lista_partida)

        while "_" in lista_partida and errores<8:
            letra=input("Introduce una letra: ")
            if letra in palabra_secreta:
                for x in range(len(palabra_secreta)):
                    if palabra_secreta[x]==letra:
                        lista_partida[x]=letra
                lista_aciertos.append(letra)
                num_aciertos=len(lista_aciertos)
            else:
                print("La letra que has introducido no esta en la palabra")
                print("".join(lista_ahorcado[:errores]))
                lista_errores.append(letra)
                num_errores=len(lista_errores)
            print(*lista_partida)
            if "_" not in lista_partida:
                print("¡Has ganado!")
                print("Has acertado",num_aciertos,"letras")
                print("Has fallado",num_errores,"veces")
                print("Has tardado",redondear_tiempo,"segundos en adivinar la palabra")
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
while cronometro in ["no", "n", "No", "NO"]:
    while repetir in ["si","sí", "s", "S", "Si", "SI"]:
        lista_partida=[]
        lista_aciertos=[]
        lista_errores=[]
        palabra_secreta=random.choice(lista_palabrasecreta)
        print(palabra_secreta)
        lista_palabrasecreta.remove(palabra_secreta)

        for x in palabra_secreta:
            lista_partida.append("_")
        print(*lista_partida)

        while "_" in lista_partida and errores<8:
            letra=input("Introduce una letra: ")
            if letra in palabra_secreta:
                for x in range(len(palabra_secreta)):
                    if palabra_secreta[x]==letra:
                        lista_partida[x]=letra
                lista_aciertos.append(letra)
                num_aciertos=len(lista_aciertos)
            else:
                print("La letra que has introducido no esta en la palabra")
                print("".join(lista_ahorcado[:errores]))
                lista_errores.append(letra)
                num_errores=len(lista_errores)
            print(*lista_partida)
            if "_" not in lista_partida:
                print("¡Has ganado!")
                print("Has acertado",num_aciertos,"letras")
                print("Has fallado",num_errores,"veces")
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
                nuevas_palabras=input("¿Quieres añadir nuevas palabras al juego? (si/no): ")
                if nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                    while nuevas_palabras in ["si","sí", "s", "S", "Si", "SI"]:
                        nueva_palabra=input("Introduce la nueva palabra: ")
                        lista_palabrasecreta.append(nueva_palabra)
                        nuevas_palabras=input("¿Quieres añadir otra palabra? (si/no): ")
                repetir=input("¿Quieres jugar otra vez? (si/no): ")
                if repetir not in ["si","sí", "s", "S", "Si", "SI"]:
                    print("¡Hasta la próxima!")
                


