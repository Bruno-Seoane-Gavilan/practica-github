var1="0"
listaprecio=[]
listastock=[]
precio_total=0

listaproductos=[]

lista1=var1.split("-")
for x in lista1:
    lista2=x.split(":")
    listaproductos.append(lista2[0])
    listaprecio.append(lista2[1])
    listastock.append(lista2[2])
listaprecio=[int(x) for x in listaprecio]
listastock=[int(x) for x in listastock]
for j in range(len(listaproductos)):
    precio_total=precio_total+(listaprecio[j]*listastock[j])
print(precio_total)
mascaro=max(listaprecio)
posicion=listaprecio.index(mascaro)
print(listaproductos[posicion])
posicion=listaprecio.index(0)
print(listastock[posicion])
listaprecio.pop(posicion)
listastock.pop(posicion)
listaproductos.pop(posicion)
print(listaproductos)