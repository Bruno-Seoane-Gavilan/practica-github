
#Al principio del programa se declaran todas las variables que vamos a usar
dni=""
dni_resultante=[]
repetir="s"
letras_posibles_dni="TRWAGMYFPDXBNJZSQVHLCKE"
letra_dni=""
lista_intentos=[]
dni_correctos=[]
dni_incorrectos=[]
opcion_menu=""
dni_final=[]
total_errores=0
#Después hacemos que el programa divida el DNI entre 23 y segun el resultado se le asigne una letra
while repetir == "s":
    dni=input("Introduce un DNI: ")
    if not(len(dni)== 8):
        print("El DNI no tiene la longitud correcta")
        dni_incorrectos.append(dni)
        lista_intentos.append(0)
        total_errores=total_errores+1
    elif not dni.isdigit():
        print("El DNI tiene que ser solo números")
        dni_incorrectos.append(dni)
        lista_intentos.append(1)
        total_errores=total_errores+1
    else:
        resto_dni = int(dni) % 23
        letra_dni= letras_posibles_dni[resto_dni]
        print(dni,"-",letra_dni)
        dni_correctos.append(dni+"-" +letra_dni)
        lista_intentos.append(3)
    #Preguntamos si quiere volver a introdducir otro dni para calcularle la letra
    lista_intentos.append(3)
    lista_intentos.append(2)
    repetir=input("¿Quieres volver a introducir otro DNI? s/n: ")
dni_correctos.sort()
dni_incorrectos.sort()
total_dni_correctos=len(dni_correctos)
total_dni=total_dni_correctos+len(dni_incorrectos)
porcentaje_dni_correctos=(total_dni_correctos/total_dni)*100
porcentaje_dni_incorrectos=(len(dni_incorrectos)/total_dni)*100
porcentaje_errores_longitud=(lista_intentos.count(0)/total_dni)*100
porcentaje_errores_numero=(lista_intentos.count(1)/total_dni)*100
#Aquí empieza el menú de opciones
print("Menú de opciones:")
print("1. Listar DNI correcto ordenado de menor a mayor")
print("2. Listar DNI incorrecto ordenado de menor a mayor")
print("3. Número total de errores producidos")
print("4. Número total de DNI correctos")
print("5. Porcentajes intentos con error y sin error")
print("6. Salir s/n")
while not (opcion_menu=="6"):
    opcion_menu=input("Elige una opción entre 1 y 6: ")
#Aqui es donde se muestra la opción que quiere del menú
    if opcion_menu=="1":
        print("DNI correctos ordenados de menor a mayor:",dni_correctos)
    elif opcion_menu=="2":
        print("DNI incorrectos ordenados de menor a mayor:",dni_incorrectos)
    elif opcion_menu=="3":
        print("Número total de errores producidos:",total_errores)
    elif opcion_menu=="4":
        print("Número total de DNIs correctos:",total_dni_correctos)
    elif opcion_menu=="5":
        print("Porcentajes de intentos con error y sin error:")
        print("Porcentaje de DNI correctos:",porcentaje_dni_correctos,"%")
        print("Porcentaje de DNI incorrectos:",porcentaje_dni_incorrectos,"%")
        print("Porcentaje de errores de longitud:",porcentaje_errores_longitud,"%")
        print("Porcentaje de errores de número:",porcentaje_errores_numero,"%")
#Aqui si quiere la opción 6 el programa se acaba
    elif opcion_menu=="6":
        print("Programa finalizado.")
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 6.")