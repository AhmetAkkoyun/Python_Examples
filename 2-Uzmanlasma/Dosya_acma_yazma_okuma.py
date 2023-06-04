# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:41:07 2021

@author: ahmet
"""

##########################################
##                                      ##
##  Metin Dosyası Açma / Yazma / Okuma  ##
##                                      ##
##########################################

import os
"""
print(os.listdir())     # mevcut dizindeki dosyaları listeler

# yeni bir metin dosyası oluşturma

ogrenci_dosya = os.open("ogrenciler.txt", os.O_RDWR|os.O_CREAT)

# os.O_RDWR komutu okumaya ve yazmaya yetkili olarak açmak için
# os.O_CREAT dosya oluşturmak için
# arasına | işareti koyduk. önce dosyayı aç eğer yoksa oluştur demek için



# dosyanın içini dolduralım

os.write(ogrenci_dosya, "Ali Er, 70\n".encode())
os.write(ogrenci_dosya, "Mehmet Kaya, 50\n".encode())
os.write(ogrenci_dosya, "Ayşe Su, 100\n".encode())
os.write(ogrenci_dosya, "Nihan Korkmaz, 90\n".encode())

# bir str girmek istersek sonuna .encode() eklemeliyiz
 
os.close(ogrenci_dosya) # işimiz bitince dosyayı kapatıyoruz
"""

# ogrenciler.txt dosyasında bulunan metni okuyacağız

ogrenci_dosya = os.open("ogrenciler.txt", os.O_RDONLY) # RDONLY sadece okuma

dosya_uzunluk = os.stat(ogrenci_dosya).st_size  

# pythonda bir dosyanın okunması için onun kaç byte olduğu bilinmelidir
# yukarıdaki komutta dosyanın kaç byte olduğu bilgisini
# bulduk ve dosya_uzunluk olarak kaydettik

icerik = os.read(ogrenci_dosya, dosya_uzunluk)

# dosya içeriğini bir içerik değişkenine kaydettik

print(icerik.decode())  # yazarken .encode() eklediğimiz gibi .decode() ekle

os.close(ogrenci_dosya)



# dosya silmek için 

"""
os.unlink("ogrenciler.txt")
"""




