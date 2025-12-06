#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
import random
numero_dado=0
veces_uno=0
veces_dos=0
veces_tres=0
veces_cuatro=0
veces_cinco=0
veces_seis=0
tiradas=0
while not (tiradas>=100):
    numero_dado=random.randint(1,6)
    if numero_dado==1:
        veces_uno=veces_uno+1
    if numero_dado==2:
        veces_dos=veces_dos+1
    if numero_dado==3:
        veces_tres=veces_tres+1
    if numero_dado==4:
        veces_cuatro=veces_cuatro+1
    if numero_dado==5:
        veces_cinco=veces_cinco+1
    if numero_dado==6:
        veces_seis=veces_seis+1
    tiradas=tiradas+1
print("Uno: ",veces_uno)
print("Dos: ",veces_dos)
print("Tres: ",veces_tres)
print("Cuatro: ",veces_cuatro)
print("Cinco: ",veces_cinco)
print("Seis: ",veces_seis)