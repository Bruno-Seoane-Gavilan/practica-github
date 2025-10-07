
#división con 2 decimales 
division_2_decimales=format(división, ".2f")

#Para redonder a 2 decimales
var1=round(división, 2)


#Variable numérica
var1=4
#Variable decimal
var2=4.5
#Variable de texto
var3="hola"


#Print sirve para mostrar información por pantalla
print("El resultado el número es: ", var1)


#Int sirve para convertir una variable a número entero
var1=int(input("introduce un número: "))
#Float sirve para convertir una variable a número decimal
var2=float(input("introduce otro número: "))
#Input sirve para pedir información al usuario
var3=input("introduce un texto: ")


#Operadores aritméticos
suma=var1+var2
resta=var1-var2
multiplicación=var1*var2
división=var1/var2
divisiónentera=var1//var2
módulo=var1%var2
exponenciación=var1**var2
print("El resultado de la suma es: ", suma)


#para usar condicionales
if var1==var2:
    print("var1 es igual que var2")
else:
    print("var1 no es igual que var2")

#para usar raiz cuadrada
import math
raiz_cuadrada=math.sqrt(var1)
print("La raíz cuadrada de var1 es: ", raiz_cuadrada)

#para usar el número pi
import math
pi=math.pi
print("El valor de pi es: ", pi)

#para usar el condicional
#el condicional elif sirve para poner una condición entre el if y el else
if var1>var2:
    print("var1 es mayor que var2")
elif var1<var2:
    print("var1 es menor que var2")
else:
    print("var1 es igual que var2")

#operadores de condicionales
== igual
!= diferente
> mayor que
< menor que
>= mayor o igual que
<= menor o igual que

#operadores lógicos
and y
or o
not no 

#letra.isupper() sirve para saber si una letra es mayúscula
#letra.islower() sirve para saber si una letra es minúscula
#letra.isnumeric() sirve para saber si una letra es un número (solo dígito)
#letra.isalpha() sirve para saber si una letra es alfabética (solo letra)
#letra.isalnum() sirve para saber si una letra es alfanumérica (letra o número)
#letra.isspace() sirve para saber si una letra es un espacio en blanco


if letra.isupper():
    print("La letra es mayúscula: True")

#len(frase) sirve para saber la longitud de una frase o texto
longitud=len(frase)

#para que sirve el método index
frase.index(palabra) sirve para saber la posición de una palabra en una frase
