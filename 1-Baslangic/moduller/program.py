# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:40:34 2021

@author: ahmet
"""

#################
##             ## 
##  ANA MODUL  ## 
##             ## 
#################

import aritmetik
import mesaj

mesaj.mesaj_yaz("hoşgeldiniz")
print("")
print("Yapabileceğiniz işlemler:")
print("")

print("1 - toplama")
print("2 - çıkarma")
print("3 - çarpma")
print("4 - bölme")
print("5 - sayının karesi")
print("6 - sayının küpü")
print("7 - sayinin kökü")
print("8 - ortalama hesabı")
print("9 - işaret değiştirme")

secilen_islem = int(input("lütfen yapmak istediğiniz işlem numarasını giriniz: "))

if secilen_islem == 1:
    a=int(input("toplama işlemi için ilk sayıyı giriniz: "))
    b=int(input("toplama işlemi için ikinci sayıyı giriniz: "))
    print("\n\nsonuç", aritmetik.topla(a,b))
elif secilen_islem == 2:
     a=int(input("çıkarma işlemi için ilk sayıyı giriniz: "))
     b=int(input("çıkarma işlemi için ikinci sayıyı giriniz: "))
     print("\n\nsonuç", aritmetik.cikar(a,b))
elif secilen_islem == 3:
     a=int(input("çarpma işlemi için ilk sayıyı giriniz: "))
     b=int(input("çarpma işlemi için ikinci sayıyı giriniz: "))
     print("\n\nsonuç", aritmetik.carp(a,b))
elif secilen_islem == 4:
     a=int(input("bölme işlemi için ilk sayıyı giriniz: "))
     b=int(input("bölme işlemi için ikinci sayıyı giriniz: "))
     print("\n\nsonuç", aritmetik.bol(a,b))
elif secilen_islem == 5:
     a=int(input("karesini bulmak istediğiniz sayıyı giriniz: "))
     print("\n\nsonuç", aritmetik.karesini_al(a))
elif secilen_islem == 6:
     a=int(input("küpünü bulma istediğiniz sayıyı giriniz: "))
     print("\n\nsonuç", aritmetik.kupunu_al(a))
elif secilen_islem == 7:
     a=int(input("kökünü bulma istediğiniz sayıyı giriniz: "))
     print("\n\nsonuç", aritmetik.kokunu_al(a))
elif secilen_islem == 8:
     a=int(input("ortalamasını bulmak istediğiniz sayılardan ilkini giriniz: "))
     b=int(input("ortalamasını bulmak istediğiniz sayılardan ikincisini giriniz: "))
     print("\n\nsonuç", aritmetik.ortalamasini_bul(a,b))
elif secilen_islem == 9:
     a=int(input("işaretini değiştirmek istediğiniz sayıyı giriniz: "))
     print("\n\nsonuç", aritmetik.isaretini_degistir(a))
     
     
     
print("")
mesaj.mesaj_yaz("Hoşçakalın")

