year=int(input())
if year%4==0 and not(year%100==0) or (year%100==0 and year%400==0):
#Aqui se hace la división para combrobar se es bisiesto(divisible entre 4 y no entre 100) o no lo es.
    print("YES")
else:
    print("NO")