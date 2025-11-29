#40. Crea un programa que cuente todos los números pares hasta el número 

total_par=0
total_inpar=0
for j in range(0,50,2):
    total_par=total_par+1
for j in range(1,50,2):
    total_inpar=total_inpar+1
print("El total de pares es:",total_par)
print("El total de inpares es:",total_inpar)
