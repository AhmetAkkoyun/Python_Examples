sayilar = [17,23,15,75,55,30,10,21,20,34,28,107,5,4,32]
sayac = 0
for sayi in sayilar:
    if sayi%5 == 0:
        print(sayi, ": 5'in katıdır.")
        sayac = sayac+1
    
# Döngü sonu

print("5'in katı olan sayı adeti : "+str(sayac))