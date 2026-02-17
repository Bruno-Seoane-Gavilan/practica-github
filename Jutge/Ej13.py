import math
x=float(input(""))
#El float para que el número pueda ser decimal.
floor=math.floor(x)
#El floor sirve para que se redondee el número hacia abajo.
ceil=math.ceil(x)
#El ceil sirve para que se redondee el número hacia arriba.
if x-floor<ceil-x:
    print(floor,ceil,floor)
elif not(x-floor<ceil-x):
    print(floor,ceil,ceil)
else:
    print(floor,ceil,ceil)
#Mira si hay más distancia entre el floor o el ceil y si es igual, se redondea hacia arriba.