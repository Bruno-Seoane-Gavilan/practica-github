#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While

num_1=0
num_2=0
repetir="s"
suma=num_1 + num_2
repeticiones=0
cont_sumas=0
while repetir=="s":
    num_1=int(input("Introduce el primer número: "))
    num_2=int(input("Introduce el segundo número: "))
    repeticiones=repeticiones+1
    suma=num_1+num_2
    cont_sumas=cont_sumas+suma
    print("La suma de los dos números es: ",suma)
    repetir=input("Deseas repetir la operación s/n: ")
print("Programa finalizado")
print("Has hecho",repeticiones,"repeticiones")
print("El total de todas las sumas es: ",cont_sumas)