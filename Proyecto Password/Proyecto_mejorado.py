#1.En esta versión, no debes contemplar que se cumplan las condiciones en las posiciones de los índices, pero sí que el total de criterios se cumplan: 3 números (distinguiendo rangos), 3 letras (distinguiendo mayúsculas o minúsculas), 2 símbolos, etc.
#2.Tiene que existir un for que recorra el password y realice las comprobaciones y los contajes necesario.
#3.El usuario debe poder introducir un total de 3 passwords en una misma ejecución del programa. Además de visualizar por pantalla si el password cumple o no con los criterios, debe aparecer por pantalla el número de passwords que ha introducido con formato correcto e incorrecto.

password_correcto=0
password_incorrecto=0
for intento in range(3):
    print("Introduce una contraseña de entre 6 y 8 caracteres que respete lo siguiente:")
    print("Tiene que haber 3 números del 1 al 9")
    print("Tiene que haber 2 letras minúsculas")
    print("Tiene que haber 1 letra mayúscula")
    print("Tiene que haber 2 simbolos de los siguientes *, _, &, /, #")
    password=input("Introduce la contraseña:")
    longitud_password=len(password)
    error=False
    contador_numeros=0
    contador_minusculas=0
    contador_mayusculas=0
    contador_simbolos=0
    for x in password:
        if x.isdigit():
            contador_numeros=contador_numeros+1
        if x.islower():
            contador_minusculas=contador_minusculas+1
        if x.isupper():
            contador_mayusculas=contador_mayusculas+1
        if x in ['*','_','&','/','#']:
            contador_simbolos=contador_simbolos+1
    if longitud_password<6 or longitud_password>8:
        error=True
    if contador_numeros<3:
        error=True
    if contador_minusculas<2:
        error=True
    if contador_mayusculas<1:
        error=True
    if contador_simbolos<2:
        error=True
    if error==False:
        password_correcto=password_correcto+1
    else:
        password_incorrecto=password_incorrecto+1
print("Contraseñas correctas:",password_correcto)
print("Contraseñas incorrectas:",password_incorrecto)
#Contraseñas para probar:

#Corectas:
#1aB*4_6&
#5zY3/9#
#29mN*7_
#Ja3_6&1
#E2f5#8/

#Incorrectas:
#bad12
#9ZY*_
#Abcdefgh
#12345678
#aB*4_6&
