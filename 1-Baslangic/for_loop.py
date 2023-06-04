# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:45:04 2021

@author: ahmet
"""

################
##            ##
##  Döngüler  ##
##            ##
################


ogrenci_listesi = ["orhan veli", "can yücel", "cemal süreyya", "necip fazil", "nazim hikmet"]

for sairler in ogrenci_listesi:
    print(sairler)                   # sairler yerine x olabilir
    
print(len(ogrenci_listesi))

print("***********************")

# len kullanmadan listedeki eleman sayısını yazdır

sayi=0

for x in ogrenci_listesi:
    sayi = sayi + 1               # print döngünün içinde olursa
    print(sayi)                   # ekrana 1 2 3 4 5 yazar 

print("***********************")    

sayi=0
   
for x in ogrenci_listesi:
    sayi = sayi + 1               
                                  # print döngünün dışında olursa
print(sayi)                       # son sayi değeri olarak 5 yazar 


# quiz - kullanıcıdan bir isim isteyip girilen ismin öğrenci listesinde
# bulunma durumunu veren programı yazın

sinif = ["orhan veli", "can yücel", "cemal süreyya", "necip fazil", "nazim hikmet"]

aranan=input("lütfen aradığınız öğrencinin ismini ve soyismini giriniz: ")  

var = False

for x in sinif:
    if x == aranan:
        var = True
        
if var==True:
    print(aranan, "isimli öğrenci sınıfta mevcuttur")
else:
    print(aranan, "isimli öğrenci sınıfta yoktur.")

print("***********************") 
print("")
print("***********************")  

# listeler dışında for kullanımı

for i in range(10):
    print(i)