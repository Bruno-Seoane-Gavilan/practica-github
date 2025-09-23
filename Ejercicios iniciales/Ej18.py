#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.

precio_entrada = 12
descuento_adulto = 0.10
descuento_niño = 0.50

num_adultos = int(input("Introduce el número de adultos que asisten al cine: "))
num_menores = int(input("Introduce el número de menores que asisten al cine: "))

total_adultos = num_adultos * precio_entrada * (1 - descuento_adulto)
total_menores = num_menores * precio_entrada * (1 - descuento_niño)
total_pagar = total_adultos + total_menores
total_pagar = format(total_pagar, ".2f")
print("El precio total a pagar por los menores es:", total_menores, "euros.")
print("El precio total a pagar por los adulto es:", total_adultos, "euros.")