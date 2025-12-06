#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While

num_1=0
num_2=0
suma=num_1 + num_2
repeticiones=0
cont_sumas=0
while cont_sumas<=50:
    num_1=int(input("Introduce el primer número: "))
    num_2=int(input("Introduce el segundo número: "))
    repeticiones=repeticiones+1
    suma=num_1+num_2
    cont_sumas=cont_sumas+suma
    print("La suma de los dos números es: ",suma)
    print("El total de todas las sumas es: ",cont_sumas,"y llevas",repeticiones,"operaciones realizadas")
print("Fin del programa")