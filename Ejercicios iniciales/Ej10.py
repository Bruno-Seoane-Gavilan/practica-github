#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

var1_dividendo=int(input("introduce el dividendo:"))
var2_divisor=int(input("introduce el divisor: "))
var3_cociente=var1_dividendo//var2_divisor
var4_resto=var1_dividendo%var2_divisor
if var1_dividendo%2==0:
    var5_par_impar="par"
else:
    var5_par_impar="impar"
print("El cociente es:", var3_cociente)
print("El resto es:", var4_resto)
print("El dividendo es:", var5_par_impar)