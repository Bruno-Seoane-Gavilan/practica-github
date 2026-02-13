import math
x=float(input(""))
floor=math.floor(x)
ceil=math.ceil(x)
if x-floor<ceil-x:
    print(floor,ceil,floor)
elif not(x-floor<ceil-x):
    print(floor,ceil,ceil)
else:
    print(floor,ceil,ceil)