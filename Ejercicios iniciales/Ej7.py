#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedesforzar que el resultado de la división tenga 2 decimales?
var1=int(input("introduce un número: "))
var2=int(input("introduce otro número: "))


resultadosuma=var1+var2
resultadoresta=var1-var2
resultadomultiplicación=var1*var2
resultadodivision=var1/var2
resultadodivisionentera=var1//var2
resultadomódulo=var1%var2
resultadoexponenciación=var1**var2

division_2_decimales=round(resultadodivision, 2)

print("El resultado de la suma es: ", resultadosuma)
print("El resultado de la resta es: ", resultadoresta)
print("El resultado de la multiplicación es: ", resultadomultiplicación)
print("El resultado de la división es: ", division_2_decimales)
print("El resultado de la división entera es: ", resultadodivisionentera)
print("El resultado del módulo es: ", resultadomódulo)
print("El resultado de la exponenciación es: ", resultadoexponenciación)