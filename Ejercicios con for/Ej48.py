#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuariotenga x oportunidades para ver si letra introducida está en esa palabra.

palabra_secreta=input("Introduce la palabra secreta: ")
palabra_secreta=str(palabra_secreta.lower())
letra="hola"
for j in range (len(palabra_secreta)):
    letra=input("Introduce una letra de la palabra secreta: ")
    if palabra_secreta.__contains__(letra):
        print("La letra existe")
    else:
        print("La letra no existe")