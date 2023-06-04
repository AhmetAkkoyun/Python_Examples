# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:48:52 2021

@author: ahmet
"""

class kara_araci():
    hiz = 0
    def __init__(self, beygir_gucu, teker_sayisi):
        self.beygir_gucu = beygir_gucu
        self.teker_sayisi = teker_sayisi
    
    def hizi_ayarla(self, hiz_degeri):
        self.hiz = hiz_degeri
        

class otobus(kara_araci):
    def __init__(self, beygir_gucu, teker_sayisi, yolcu_kapasitesi):
        kara_araci.__init__(self, beygir_gucu, teker_sayisi)
        self.yolcu_kapasitesi = yolcu_kapasitesi
        

otobus1 = otobus(500, 8, 44)

print(otobus1.beygir_gucu)



class araba(kara_araci):
     def __init__(self, beygir_gucu, teker_sayisi, sunroof):
        kara_araci.__init__(self, beygir_gucu, teker_sayisi)
        self.sunroof = sunroof

otomobil1 = araba(120, 4, "sunroof var")

print(otomobil1.beygir_gucu, otomobil1.sunroof)


print("*****************************************************")

otomobil1.hizi_ayarla(70)   # kara aracindan def çekiyoruz

print(otomobil1.hiz)




