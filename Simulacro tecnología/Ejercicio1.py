inicio=int(input("Introduce el inicio: "))
fin=int(input("Introduce el fin: "))
incremento=int(input("Introduce el incremento: "))
concatenar=""

for x in range (inicio,fin,incremento):
    if not x%4==0:
        if x%6==0:
            concatenar=concatenar+"*"+str(x)+"*"","
        else:
            concatenar=concatenar+str(x)+","
print(concatenar[:-1])
        