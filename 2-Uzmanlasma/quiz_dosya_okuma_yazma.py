# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:24:45 2021

@author: ahmet
"""

###########################
##                       ##
##         Quiz          ##
##  Dosya Okuma / Yazma  ##
##                       ##
###########################


# bir önceki ders oluşturduğumuz "ogrenciler.txt isimli dosyada bulunan
# öğrencilerin not ortalamalarını hesaplayan programı yazınız



# çözüm 
# öncelikle programın dosyayı okumasını sağlamalıyız.
# ardından listeler yardımı ile okunan ifadeleri parçalayabiliriz

import os

ogrenciler_dosya = os.open("ogrenciler.txt", os.O_RDONLY)
dosya_uzunluk = os.stat(ogrenciler_dosya).st_size
icerik = os.read(ogrenciler_dosya, dosya_uzunluk)

ogrenciler = icerik.decode()


ogrenci_list = ogrenciler.split("\n")

ogrenci_sayisi = len(ogrenci_list)-1  # sonda bir satır boşluk var oyüzden -1


# şimdi elimizde "ogrenci adi, notu" şeklinde sıralanmış bir liste var 
# bu listeden notları çekmek gerek 
# listeyi teker teker okutup notları çekeceğiz
# while ya da for kullanılabilir


"""
x = 0

while x < ogrenci_sayisi           :
    print(ogrenci_list[x])
    x = x+1
    
# bu ifadeyi çalıştırırsak while komutunun ogrenci_list dizisini teker teker
yazdırdığını görebiliriz. 
# ama biz yazdırmak yerine teker teker böldürelim 
# o zaman print komutunun olduğu yere içinde split olan bir komut eklersek
# amacımıza ulaşırız
    
"""

x = 0
toplam_notlar = 0
while x < ogrenci_sayisi           :
    ogrenci_notu = ogrenci_list[x].split(",")  
# ogrenci_list dizisindeki her bir elemanı virgülden ayır ve 
# ogrenci_notu isimli yeni diziye kaydet
 
    toplam_notlar = toplam_notlar + (int(ogrenci_notu[1])) 
# dizideki 1. (yani 2) karakterleri döngü boyunca int olarak toplam_notlara ekle 
    x = x+1

print("notların toplamı:", toplam_notlar)
print("ogrenci sayisi:", ogrenci_sayisi)
print("notların ortalaması:", toplam_notlar/ogrenci_sayisi)



