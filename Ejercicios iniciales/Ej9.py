#9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos=int(input("introduce un número de segundos: "))
minutos=segundos/60
horas=minutos/60

horas_dos_decimales=round(horas, 2)
minutos_dos_decimales=round(minutos, 2)

print("El número de minutos es:", minutos_dos_decimales,"y", "el número de horas es:", horas_dos_decimales)