#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

nota=float(input("Introduce la nota (entre 0 y 10): "))

if nota < 0:
    print("La nota que has introducido no esta entre 0 y 10.")
elif nota > 10:
    print("La nota que has introducido no esta entre 0 y 10.")
elif nota >= 8.5:
    print("Tu nota es un:", nota, "has sacado un excelente")
elif nota >= 6.5:
    print("Tu nota es un:", nota, "has sacado un notable")
elif nota >= 5:
    print("Tu nota es un:", nota, "has sacado un satisfactorio")
else:
    print("Tu nota es un:", nota, "has sacado un insuficiente")