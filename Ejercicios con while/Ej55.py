#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

num_1=0
num_2=0
suma=num_1 + num_2
repeticiones=0
cont_sumas=0
while cont_sumas<=50 or float(cont_sumas/2==cont_sumas//2):
    num_1=int(input("Introduce el primer número: "))
    num_2=int(input("Introduce el segundo número: "))
    repeticiones=repeticiones+1
    suma=num_1+num_2
    cont_sumas=cont_sumas+suma
    print("La suma de los dos números es: ",suma)
    print("El total de todas las sumas es: ",cont_sumas,"y llevas",repeticiones,"operaciones realizadas")
print("Fin del programa")