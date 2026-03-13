variable=input("Introduce valores separados por comas: ")
lista=variable.split(",")
lista=[int(x) for x in lista]
print(lista)

#join

valor_maximo=max(lista)
valor_minimo=min(lista)

lista.remove(valor_maximo)
lista.remove(valor_minimo)

media=sum(lista)/len(lista)
redondeo_media=round(media,2)
print(redondeo_media)

print(lista)