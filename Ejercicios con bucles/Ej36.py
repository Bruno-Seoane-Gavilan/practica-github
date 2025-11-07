#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

numeros_naturales=int(input("Introduce el número de primeros números naturales quieres sumar: "))
numero=1
total=0
for j in range(numeros_naturales):
    total=total+numero
    numero=numero+1
print("La suma total de números naturales es: ",total)