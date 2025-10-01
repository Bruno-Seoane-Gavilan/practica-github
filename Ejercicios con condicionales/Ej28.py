#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

letra = input("Introduce una letra: ")
if letra.isupper():
    print("La letra es mayúscula: True")
elif letra.islower():
    print("La letra es minúscula: False")
elif letra.isnumeric():
    print("Has introducido un número")
else:
    print("Has introducido un símbolo")