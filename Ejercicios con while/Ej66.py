#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos.Que salgan cuantas veces sale cada número

import random
import time
inicio=time.time()
veces_uno=0
veces_dos=0
veces_tres=0
veces_cuatro=0
veces_cinco=0
veces_seis=0
while time.time()-inicio<3:
    dado=random.randint(1,6)
    if dado==1:
        veces_uno=veces_uno+1
    elif dado==2:
        veces_dos=veces_dos+1
    elif dado==3:
        veces_tres=veces_tres+1
    elif dado==4:
        veces_cuatro=veces_cuatro+1
    elif dado==5:
        veces_cinco=veces_cinco+1
    else:
        veces_seis=veces_seis+1
print("Tiempo: ", time.time()-inicio)
print("Uno",veces_uno,)
print("Dos",veces_dos,)
print("Tres",veces_tres,)
print("Cuatro",veces_cuatro,)
print("Cinco",veces_cinco,)
print("Seis",veces_seis,)