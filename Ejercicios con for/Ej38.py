#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10

numero_de_notas=int(input("Introduce el número de notas: "))
nota=0
for j in range(numero_de_notas):
    nota=float(input("introduce tu nota: "))
    if float(nota)<10 and float(nota)>1:
        if float(nota)<5:
            print("Asignatura suspendida")
        else:
            print("Asignatura aprovada")
    else:
        print("Has introducido una nota equivocada")