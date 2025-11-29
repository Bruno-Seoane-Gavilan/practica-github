password="a7e4jk"
vocales="aeiouAEIOU"
numvocales=0
total=0
for i in password:
    if i.isnumeric():
        total=total+int(i)
    if i in vocales:
        numvocales=numvocales+1
print(total)
print(numvocales)