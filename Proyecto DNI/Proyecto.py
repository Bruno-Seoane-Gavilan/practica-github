dni=""
dni_resultante=[]
repetir="s"
letras_posibles_dni="TRWAGMYFPDXBNJZSQVHLCKE"
letra_dni=""

while repetir=="s":
    dni=(input("Introduce un DNI: "))
    dni_string=str(dni)
    if not len(dni_string)==8:
        print("El DNI no tiene la longitud correcta")
    if not dni.isdigit():
        print("El DNI tiene que ser solo números")
    else:
        resto_dni=int(dni)%23
        letra_dni=letras_posibles_dni[resto_dni]
        dni_resultante.append(dni)
        dni_resultante.append(letra_dni)
        print(dni,"-",letra_dni)
    repetir=input("¿Quieres volver a introducir otro DNI? s/n: ")
        
