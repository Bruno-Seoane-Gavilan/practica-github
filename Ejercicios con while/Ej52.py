#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
num_1=0
num_2=0
repetir="s"
suma=num_1 + num_2
while repetir=="s":
    num_1=int(input("Introduce el primer número: "))
    num_2=int(input("Introduce el segundo número: "))
    suma=num_1+num_2
    print("La suma de los dos números es: ",suma)
    repetir=input("Deseas repetir la operación s/n: ")
print("Programa finalizado")