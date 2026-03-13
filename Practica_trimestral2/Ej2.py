contrasena=input("Ingrese su contraseña: ")
lista=contrasena.split()

for  x in lista:
    munletras=0
    munnumeros=0
    muncaracteres=0
    for j in x:
        if j.isnumeric():
            munnumeros+=1
        elif j.isalpha():
            munletras+=1
        else:
            muncaracteres+=1
    if muncaracteres==0 and len(x)>=8 and munletras>=1 and munnumeros>=1:
        print("La contraseña", x, "es segura")
    if muncaracteres==0 and len(x)<8 and (munletras>=1 and munnumeros==0):
        print("La contraseña", x, "es débil")
    if muncaracteres>=1:
        print("La contraseña", x, "es invalida")