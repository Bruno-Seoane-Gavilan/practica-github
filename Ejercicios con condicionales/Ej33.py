# 33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años

frase="No hay mal que dure cien años"
contador_vocales=0
frase=frase.lower()
vocales="aeiou"
for vocales in frase:
    if letra in vocales:
        contador_vocales+=1
print("El número de vocales en la frase es: ", contador_vocales)