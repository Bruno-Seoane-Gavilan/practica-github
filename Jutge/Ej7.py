temperatura=input()
if int(temperatura)<10:
    print("fa fred")
    if int(temperatura)<=0:
        print("l'aigua es gelaria")
elif int(temperatura)>30:
    print("fa calor")
    if int(temperatura)>=100:
        print("l'aigua bulliria")
elif int(temperatura)>=10 and int(temperatura)<=30:
    print("s'esta be")
    