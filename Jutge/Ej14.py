numeros=int(input())
horas=numeros//3600
minutos=(numeros%3600)//60
segundos=(numeros%3600)%60
print(horas,minutos,segundos)