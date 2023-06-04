# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:27:15 2021

@author: ahmet
"""


# bir tamsayı listesi içinde kaç tane çift sayı olduğunu bulan programı yazın




sayi_listesi1=[1, 3, 4, 6, 7, 8, 9, 10, 11, 22, 32, 45, 63, 77, 84, 102]


def cift_bul(x):
    if x%2==0:
        return(x)


                       
ciftler_listesi = list(filter(cift_bul, sayi_listesi1))
                       
print(len(ciftler_listesi))


# filter kullanmadan for döngüsü ile yap

a=0

for x in sayi_listesi1:
    if x%2==0:
        a= a+1

print(a)




# şimdi bunları otomatik yapan bir fonksiyon yaz


def listeden_cift_sayi_bul(liste):
    a=0
    for x in liste:
        if x%2==0:
            a += 1   # böyle de yazılabilir 
    return(a)
    
    
print(listeden_cift_sayi_bul(sayi_listesi1))

    
    
    
    