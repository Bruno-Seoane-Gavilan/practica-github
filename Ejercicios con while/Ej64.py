#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos

total_pares=0
total_impares=0
total_positivos=0
total_negativos=0
total_ceros=0
total_suma_numeros=0
numero=0
while not(numero==-99):
    numero=int(input("Introduce un número: "))
    if numero%2==0:
        total_pares=total_pares+1
        if numero>0:
            total_positivos=total_positivos+1
        if not(numero>0):
            total_negativos=total_negativos+1
        if numero==0:
            total_ceros=total_ceros+1
        total_suma_numeros=total_suma_numeros+numero
    else:
        total_impares=total_impares+1
        if numero%2==0:
            total_pares=total_pares+1
        if numero>0:
            total_positivos=total_positivos+1
        if not(numero>0):
            total_negativos=total_negativos+1
        if numero==0:
            total_ceros=total_ceros+1
        total_suma_numeros=total_suma_numeros+numero
    
