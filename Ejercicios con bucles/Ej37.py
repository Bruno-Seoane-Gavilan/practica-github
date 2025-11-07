#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

numero_de_notas=int(input("Introduce el número de notas: "))
nota=0
for j in range(numero_de_notas):
    nota=float(input("introduce tu nota: "))
    if float(nota)<5:
            print("Asignatura suspendida")
    else:
            print("Asignatura aprovada")
    