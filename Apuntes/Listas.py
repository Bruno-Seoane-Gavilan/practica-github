mi_lista=[1,2,3,4,5,6]
mi_lista_por2=[]
maximo=max(mi_lista)
minimo=min(mi_lista)
suma=sum(mi_lista)

print(mi_lista)
print("maximo: ",maximo)
print("minimo: ",minimo)
print("suma total: ",suma)

#for x in range(len(mi_lista)):
#    calculo=mi_lista[x]*2
#    mi_lista_por2.append(calculo)
#print(mi_lista_por2)

#for x in mi_lista:
#    mi_lista_por2.append(x*2)
#print(mi_lista_por2)

mi_lista_pro=[n*2 for n in mi_lista]
print(mi_lista_pro)