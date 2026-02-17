dinero=input("").split()
euros=int(dinero[0])
centims=int(dinero[1])
bit500=euros//500
rest_bit500=euros%500
bit200=rest_bit500//200
rest_bit200=rest_bit500%200
bit100=rest_bit200//100
rest_bit100=rest_bit200%100
bit50=rest_bit100//50
rest_bit50=rest_bit100%50
bit20=rest_bit50//20
rest_bit20=rest_bit50%20
bit10=rest_bit20//10
rest_bit10=rest_bit20%10
bit5=rest_bit10//5
rest_bit5=rest_bit10%5
mon2=rest_bit5//2
rest_mon2=rest_bit5%2
mon1=rest_mon2//1
rest_mon1=rest_mon2%1
mon50=centims//50
rest_mon50=centims%50
mon20=rest_mon50//20
rest_mon20=rest_mon50%20
mon10=rest_mon20//10
rest_mon10=rest_mon20%10
mon5=rest_mon10//5
rest_mon5=rest_mon10%5
cent2=rest_mon5//2
rest_cent2=rest_mon5%2
cent1=rest_cent2//1
rest_cent1=rest_cent2%1
print("Bitllets de 500 euros:",bit500)
print("Bitllets de 200 euros:",bit200)
print("Bitllets de 100 euros:",bit100)
print("Bitllets de 50 euros:",bit50)
print("Bitllets de 20 euros:",bit20)
print("Bitllets de 10 euros:",bit10)
print("Bitllets de 5 euros:",bit5)
print("Monedes de 2 euros:",mon2)
print("Monedes de 1 euro:",mon1)
print("Monedes de 50 centims:",mon50)
print("Monedes de 20 centims:",mon20)
print("Monedes de 10 centims:",mon10)
print("Monedes de 5 centims:",mon5)
print("Monedes de 2 centims:",cent2)
print("Monedes de 1 centim:",cent1)
