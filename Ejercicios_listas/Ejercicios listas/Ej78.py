#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir 
lista1=['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
print(lista1)
eliminado=input("Introduce el valor que deseas eliminar: ")

if eliminado.isdigit():
    eliminado_int=int(eliminado)
    if eliminado_int in [int(x) for x in lista1 if x.isdigit()]:
        lista1.remove(eliminado)
        print("Lista después de eliminar el valor", eliminado, ":", lista1)
    else:
        print("El número", eliminado, "no está en la lista.")
else:
    print("El valor introducido no es un número.")
