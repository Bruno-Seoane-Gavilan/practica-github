listanumeros=[]
listanonumeros=[]
listatodo=[]

frase=input("Introduce valores separados por un guion: ")

listatodo=frase.split("-")

for x in range(len(listatodo)):
    if listatodo[x].isnumeric():
        listanumeros.append(int(listatodo[x]))
    else:
        listanonumeros.append(listatodo[x])
print(listanumeros)
print(listanonumeros)