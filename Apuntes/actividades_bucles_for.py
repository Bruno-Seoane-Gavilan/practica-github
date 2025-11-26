
password="h1l4"
total=0 
#repeticiones=int(input("Introduce el número de veces: "))
for j in range (len(password)):
    print(password[j])
    if password[j].isnumeric():
        print("Es número")
    else:
        print("no es un número")
