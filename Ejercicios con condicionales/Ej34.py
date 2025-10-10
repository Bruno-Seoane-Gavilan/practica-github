#34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente 

var_numero1=int(input("Introduce un número: "))
var_numero2=int(input("Introduce un número: "))
var_numero3=int(input("Introduce un número: "))
var_numero4=int(input("Introduce un número: "))

var_suma =  var_numero1 + var_numero2 + var_numero3 + var_numero4
longitud=len(str(var_suma))
if var_suma % 2 == 0:     
    print("el valor de: ", var_suma, "es par")
else:
    print("el valor de: ", var_suma, "es impar")

print("La longitud de la suma es: ", longitud)

