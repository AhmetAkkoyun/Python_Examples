# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:12:17 2021

@author: ahmet
"""

############################################
##                                        ##
##  Pythonda nesneye yönelik programlama  ##
##                                        ##
############################################


class otomobil():
    klima = "klima yok"
    teker_sayisi = 4
    
    def __init__ (self, marka, model, yil, km):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.km = km
        
    def km_degisti(self, yenikm):
        self.km = yenikm

        
        
audi_oto = otomobil("audi", "a3", 2017, 18000)
opel_oto = otomobil("opel", "astra", 2015, 27000)


print(audi_oto.marka, audi_oto.model, audi_oto.yil, audi_oto.km)
print(opel_oto.marka, opel_oto.model, opel_oto.yil, opel_oto.km)

print("******************************************************")


# liste yapıp yazdıralım



satilik_arac_listesi = [audi_oto, opel_oto]

for item in satilik_arac_listesi:
    print(item.marka, item.model, item.yil, item.km)

print("******************************************************")


# eski model bir arac girelim ve klima özelliğini de girelim
# tüm araçlarda default girişimiz olan klima  yok yazısı çıkacak

sahin_oto = otomobil("tofas", "sahin", 1999, 320000)

print(audi_oto.marka, audi_oto.model, audi_oto.yil, audi_oto.km, audi_oto.klima)
print(opel_oto.marka, opel_oto.model, opel_oto.yil, opel_oto.km, opel_oto.klima)
print(sahin_oto.marka, sahin_oto.model, sahin_oto.yil, sahin_oto.km, sahin_oto.klima)  

print("******************************************************")

# audi ve opel için klima özelliğini değiştirelim
# artık girdiğimiz default özellik bu markalar için değişti

audi_oto.klima = "otomatik klima"
opel_oto.klima = "manuel klima"

print(audi_oto.marka, audi_oto.model, audi_oto.yil, audi_oto.km, audi_oto.klima)
print(opel_oto.marka, opel_oto.model, opel_oto.yil, opel_oto.km, opel_oto.klima)
print(sahin_oto.marka, sahin_oto.model, sahin_oto.yil, sahin_oto.km, sahin_oto.klima)  

print("******************************************************")

# 1 sene geçtiğini varsayalım ve yeni km değerleri girelim

audi_oto.km = audi_oto.km + 12500
opel_oto.km = opel_oto.km + 14700
sahin_oto.km = sahin_oto.km + 15000

print("1 yıl sonra")

print(audi_oto.marka, audi_oto.model, audi_oto.yil, audi_oto.km, audi_oto.klima)
print(opel_oto.marka, opel_oto.model, opel_oto.yil, opel_oto.km, opel_oto.klima)
print(sahin_oto.marka, sahin_oto.model, sahin_oto.yil, sahin_oto.km, sahin_oto.klima)  

print("******************************************************")

# değişiklikleri yukarıya fonksiyon tanımlayarak da yapabiliriz


audi_oto.km_degisti(40000)

print(audi_oto.marka, audi_oto.model, audi_oto.yil, audi_oto.km, audi_oto.klima)