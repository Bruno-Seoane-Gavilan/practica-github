edad=int(input("Introduce la edad:"))

while edad>99 or edad<=0:
    print("Edad incorrecta")
    edad=int(input("Vueve a introducir la edad:"))
print("La edad es correcta")