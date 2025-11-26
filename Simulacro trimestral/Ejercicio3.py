multiplicar=1
contador_pares=0
cifras=int(input("Introduce el número de cifras: "))

numero=int(input("Introduce un número: "))

longitud_numero=len(str(numero))

if longitud_numero==cifras:
    for x in str(numero):
        multiplicar=multiplicar * int(x)
        if int(x)%2==0:
            contador_pares=contador_pares+1
    print(multiplicar)
    print(contador_pares)
else:
    print("Longitud no correcta")
