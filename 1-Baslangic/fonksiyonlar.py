# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:09:47 2021

@author: ahmet
"""

#ekrana merhaba yazan fonksiyon
def merhaba_yaz():
    print("merhaba!")

merhaba_yaz()

#kare hesaplayıcı fonksiyon 
print("haydi kare alalım!")
def karesini_al(sayi):
    print(sayi*sayi)
    
karesini_al(int(input("karesi alinacak sayi:")))

#kök hesaplayıcı fonksiyon 
print("şimdi kök alalım!")
def kokunu_al(sayi):
    return sayi**(1/2)
    
kok=kokunu_al(int(input("koku alinacak sayi:")))
    
print(kok)


#iki parametreli fonksiyon
print("teşekkürler! şimdi sizi tanıyalım!")
def isim_yas(isim,yas):
    print("\nadınız:", isim, "ve yaşınız:", yas)

isim_yas((input("isminizi giriniz:")),(input("yasinizi giriniz:")))

print("tanıştığımıza memnun oldum!")


#cift mi tek mi
print("\n\nşimdi tek ve çift sayıları bulalım!")
def tekmi_ciftmi(sayi):
    if(sayi%2==0):
        print("cift")
    else:
        print("tek")
        
tekmi_ciftmi(int(input("\nbir sayi giriniz:")))
tekmi_ciftmi(int(input("\nbir sayi daha giriniz:")))
tekmi_ciftmi(int(input("\nnasil da biliyorum ama! bir sayi daha giriniz:")))
tekmi_ciftmi(int(input("\nson kez sayi giriniz:")))
print("\nharikayim! süperim! resmen zeka küpüyüm!\nhem de yapay zeka!")




































