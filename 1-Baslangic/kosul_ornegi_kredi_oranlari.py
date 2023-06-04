# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:51:27 2021

@author: ahmet
"""


#kredi oranı 
#0-50000 %1,65
#50000-100000 %1.35
#100000 üzeri %1.05


kredi_miktari=int(input("istediğiniz kredi miktarını giriniz:"))
if(kredi_miktari<50000):
    print("kredi faiz oranı: %1,65")
elif(kredi_miktari>=50000) and (kredi_miktari<100000):
    print("kredi faiz oranı: %1,35")
else:
    print("kredi faiz oranı: %1,05")    
    
print("hoşçakalın...")

