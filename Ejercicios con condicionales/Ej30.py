

frase=input("Introduce una frase:")
longitud=len(frase)

if longitud > 11:
    print("La frase tiene 11 caracteres o más")
elif longitud <11:
    print("La frase tiene menos de 11 caracteres")
else:
    print("La frase tiene 11 caracteres exactos")

