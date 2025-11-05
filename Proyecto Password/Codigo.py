
#Antes de pedir que imtroduzca la contraseña primero hago que printee todas las caracteristicas que tiene que tener esta contraseña
print("Introduce una contraseña de entre 6 y 8 caracteres que cumpla con lo siguiente:")

print("Posición 1: Un número mayor o igual 1 y menor o igual que 5")
print("Posición 2: Una letra minúscula")
print("Posición 3: Una letra mayúscula")
print("Posición 4: Uno de los siguientes simbolos *, _")
print("Posición 5: Una letra minúscula")
print("Posición 6: Un número mayor o igual 6 y menor o igual que 9")
print("Posición 7: Uno de los siguientes simbolos &,/, #")
print("Posición 8: Un número menor o igual que 5")

#Aqui se pide que introduzca la contraseña
password=input("Introduce la contraseña:")

#Con len() el programa mide la longitud del password
longitud_password=len(password)
error=False

#Comprueba si el primer digitoo es un número y que sea mayor que 5 y menor que 8
if longitud_password <=5 or longitud_password>= 9:
    print("Error, el password tiene una longitud de",longitud_password,"que no es la que se ha pedido")
# Aqui es donde empiezan las indicaciones para ver si se cumplen todas las caracteristicas que tiene que tener este password
else:
    if not (password[0].isdigit() and int(password[0])>=1 and int(password[0])<=5):
        print("Error en el caracter 1")
        error=True
    if not (password[1].islower()):
        print("Error en el caracter 2")
        #Utilizo el error=true para que despues si al final el error es igual a false que diga que la contraseña es correcta
        error=True
    if not (password[2].isupper()):
        print("Error en el caracter 3")
        error=True
    if not (password[3]=="*" or password[3]=="_"):
        print("Error en el caracter 4")
        error=True
    if not (password[4].islower()):
        print("Error en el caracter 5")
        error=True
    if not (password[5].isdigit() and int(password[5])>=6 and int(password[5])<=9):
        print("Error en el caracter 6")
        error=True
    if len(password)>6:
        if not (password[6]=="&" or password[6]=="/" or password[6]=="#"):
            print("Error en el caracter 7")
            error=True
    if len(password)>7:
        if not (password[7].isdigit() and int(password[7])<=5):
            print("Error en el caracter 8")
            error=True
    if error==False:
        #Aqui es donde dice que si error= false solo printea los errores pero no printea que la contraseña es correcta eso solo lo hará si error=false
        print("La contraseña es correcta")