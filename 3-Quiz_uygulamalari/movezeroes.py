# -*- coding: utf-8 -*-

def moveZeroes(sayilar):    
    j = 0
    for sayi in sayilar:
        if(sayi != 0):
            sayilar[j] = sayi
            j += 1

    for x in range(j, len(sayilar)):
        sayilar[x] = 0


sayilar = [0,1,0,3,11]
moveZeroes(sayilar)
print(sayilar)