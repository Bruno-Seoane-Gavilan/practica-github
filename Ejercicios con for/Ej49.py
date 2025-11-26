#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

palabra_secreta=input("Introduce la palabra secreta: ")
palabra_secreta=str(palabra_secreta.lower())
letra="hola"
for j in range (len(palabra_secreta)):
    letra=input("Introduce una letra de la palabra secreta: ")
    if palabra_secreta.__contains__(letra):
        print("La letra existe")
        print("y esta en la posición", palabra_secreta.index(letra)+1)
    else:
        print("La letra no existe")