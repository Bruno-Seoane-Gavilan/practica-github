horas, minutos, segundos=map(int, input().split())
#Utilizo el map para que la variable horas, minutos y segundos se asignen cada una al primer valor horas, al segundo valor minutos y al tercero segundos.
segundos=segundos+1
#Suma un segundo.
if segundos==60:
    segundos=0
    minutos=minutos+1
#Si los segundos son 60, se ponen a 0 y se suma un minuto.
if minutos==60:
    minutos=0
    horas=horas+1
#Si los minutos son 60, se ponen a 0 y se suma una hora.
if horas==24:
    horas=0
#Si las horas son 24, se ponen a 0.
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
#El 02d sirve para que si el digito es más pequeño que 10, se añada un 0 delante.
#La f sirve para que se escriba sin espacios de por medio.