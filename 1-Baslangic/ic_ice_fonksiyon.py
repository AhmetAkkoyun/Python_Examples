# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:47:56 2021

@author: ahmet
"""

# sayının karesini alıp ekrana yazdırmak

def ekrana_yazdir(yazdir):
    print(yazdir)

def karesini_al(sayi):
    karesi = sayi**2
    ekrana_yazdir(karesi)  #ilk fonksiyonu burada içeri yazdık
    
karesini_al(int(input("karesini istediğiniz sayıyı giriniz:")))


#sayının karesini ve küpünü aynı anda almak

def sayinin_karesi_kupu(sayi):
    karesi=sayi*sayi
    kupu=sayi*sayi*sayi
    return karesi, kupu

girilensayi= int(input("bir sayi giriniz:"))
sayinin_karesi, sayinin_kupu = sayinin_karesi_kupu(girilensayi)
print("sayinin karesi:", sayinin_karesi, "sayinin kupu:", sayinin_kupu)


