horas, minutos, segundos=map(int, input().split())
#el map sirve para asignar el primer valor a horas, el segundo a minutos y el tercero a segundos.
segundos=segundos+1
if segundos==60:
    segundos=0
    minutos=minutos+1
if minutos==60:
    minutos=0
    horas=horas+1
if horas==24:
    horas=0
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
#la f sirve para que lo que salga, salga todo junto sinespacios de por medio.
#El 02d sirva para que si hay un número entre 0 y 9, salga con un 0 delante.