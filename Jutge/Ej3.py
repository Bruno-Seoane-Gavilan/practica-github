numero=input()
if numero=="2":
    num=input()
    sum=int(numero)+int(num)
    print(sum)
else:
    lista=numero.split()
    sum=int(lista[0])+int(lista[1])
    print(sum)