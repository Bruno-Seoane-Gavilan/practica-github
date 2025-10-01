#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla

letra = input("Introduce una letra: ")
if letra.isupper():
    print("La letra es mayúscula: True")
elif letra.islower():
    print("La letra es minúscula: False")
elif letra.isnumeric():
    print("Has introducido un número")
else:
    print("La letra es mayúscula ¿?")