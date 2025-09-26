#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10

var1=int(input("Introduce un número entre 0 y 10: "))
var2=int(input("Introduce otro número entre 0 y 10: "))

if (var1<0 or var1>10) or (var2<0 or var2>10):
    print("Uno o los dos numeros estan fuera de los límites permitidos")
elif var1>var2:
    print("El número:",var1, "es mayor que:", var2)

elif var1<var2:
    print("El número:", var2, "es mayor que:", var1)

else:
    print("Ambos números son iguales")
