#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math

raiz_cuadrada = float(input("Introduce un número para calcular su raíz cuadrada: "))
raiz = math.sqrt(raiz_cuadrada)

raiz_entero = raiz // 2
raiz = round(raiz, 2)

print("La raíz cuadrada de", raiz_cuadrada, "es:", raiz)
print("La raíz cuadrada de", raiz_cuadrada, "dividida entre 2 es:", raiz_entero)