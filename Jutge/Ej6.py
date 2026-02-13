num=input()
num=num.split()
if int(num[0])>int(num[1]) and int(num[0])>int(num[2]):
    print(num[0])
if int(num[1])>int(num[0]) and int(num[1])>int(num[2]):
    print(num[1])
if int(num[2])>int(num[0]) and int(num[2])>int(num[1]):
    print(num[2])
if int(num[0])==int(num[1]) and int(num[0])>int(num[2]):
    print(num[0])
if int(num[0])==int(num[2]) and int(num[0])>int(num[1]):
    print(num[0])
if int(num[1])==int(num[2]) and int(num[1])>int(num[0]):
    print(num[1])
if int(num[0])==int(num[1]) and int(num[0])==int(num[2]):
    print(num[0])