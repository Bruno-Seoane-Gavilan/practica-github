#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

dividendo=int(input("introduce el dividendo: "))
divisor=int(input("introduce el divisor: "))
cociente=dividendo//divisor
resto=dividendo%divisor
if dividendo%2==0:
    par_impar="par"
else:
    par_impar="impar"
print("El cociente es:", cociente)
print("El resto es:", resto)
print("El dividendo es:", par_impar)