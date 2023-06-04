# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:27:08 2021

@author: ahmet
"""

##########################
##                      ##
##  Programlama Sınavı  ##
##                      ##
##########################


print("******daire yarıçapından alan ve çevre bulma********")

"""
Bir dairenin yarıçapını kullanıcıdan alarak alanını ve 
çevresini hesaplayan ve ekrana yazdıran kodu yazınız. 
Formüller: Alan= π*r² – Çevre=2*π*r

Π = 3.14 olarak kabul edilebilir.
"""
"""
import math

r = int(input("Lütfen dairenin yarıçapını cm cinsinden giriniz: "))
print("yarıçapı", r, "cm olan dairenin alanı:", round((math.pi)*(r**2), 2), "cm karedir")
print("yarıçapı", r, "cm olan dairenin çevresi:", round(2*(math.pi)*r, 2), "cmdir")
"""

print("********öğrenci numarasından bilgi çekme******************")

"""
Öğrencilerine 12 haneli öğrenci numarası veren üniversitenin 
verdiği numaranın ilk 4 hanesi giriş yılı 5. ve 6. hanesi 
okuduğu fakültenin numarası 7. ve 8. hane bölüm numarası 
9. hanesi öğrenim numarası 11. ve 12. hane ise öğrencinin 
üniversiteye giriş sırasıdır. 12 haneli öğrenci kodunu 
kullanıcıdan alarak anlamlı şekilde ayıran ve ekrana yazan 
kodu yazınız.
"""
"""
ogrenci_no = input("Lütfen 12 haneli öğrenci numaranızı giriniz :")

while len(ogrenci_no) != 12:
    ogrenci_no = input("Lütfen 12 haneli öğrenci numaranızı giriniz :")

print("Öğrenci No   :", ogrenci_no)
print("Giriş Yılı   :", ogrenci_no[0:4])
print("Fakülte No   :", ogrenci_no[4:6])
print("Bölüm No     :", ogrenci_no[6:8])
print("Öğrenim No   :", ogrenci_no[8:10])
print("Giriş Sırası :", ogrenci_no[10:12])
"""

print("*****girilen bir sayının tam böldüğü liste elemanlarını bulma******")

"""
Bir liste içindeki 5’in katları olan sayıları bulan ve 
ekrana yazan bir program yazınız.
"""

"""
list1 = []
a = input("oluşturmak istediğiniz listeye sayı ekleyiniz : ")

while a != "tamam":
    list1 = list1 + [a]
    a = input("oluşturmak istediğiniz listeye bir sayı daha ekleyiniz (bitirmek için tamam yazınız) : ")
    
    
print("oluşturduğunuz liste :", list1)

x = int(input("oluşturduğunuz listede hangi sayının katlarını bulmak istersiniz? :"))

list2 = []
for i in list1:
    if int(i)%x==0:
        list2 = list2 + [i]

print("oluşturduğunuz dizide", x, "ile tam bölünen sayılar:", list2, "dir")        
"""        
        
print("******listeden eleman kaydırma*****")

"""
Parametre olarak bir tamsayı dizisi alan bir fonksiyon yazın 
(fonksiyonun adi moveZeroes olsun). Bu fonksiyonun görevi bu 
tamsayı dizisindeki sıfır olmayan öğelerin göreli sırasını 
korurken, tüm 0'ları dizinin sonuna taşısın.

Not: Bunu dizinin bir kopyasını oluşturmadan, 
aynı dizi üzerinde yapmanız gerekmektedir.
"""
"""
list2 = []
a = input("oluşturmak istediğiniz listeye sayı ekleyiniz : ")


while a != "*":
    list2 = list2 + [a]
    a = input("bir sayı daha ekleyiniz (bitirmek için *) : ")


k = input("sona ötelenmesini istediğiniz sayıyı girin:")

print("girdiğiniz dizi listesi:\n",list2) 


def moveZeroes(x):
    for i in x:
        if i==k:
            x.append(i)            
            x.remove(i)                       
    return(x)

moveZeroes(list2)

print("dizinin düzenlenmiş hali:\n", list2)
"""

print("***********")

"""
Parametre olarak bir tamsayı listesi/arrayi (lst) alan bir fonksiyon yazın
(fonksiyonun adı validMountainArray olsun). Bu fonksiyonun görevi lst 
tamsayı listesi eğer geçerli bir mountain array ise true değerini 
döndürsün aksi halde false değerini döndürsün.
"""



def validMountainArray(x):
    a = 0
    for i in range(len(x)):
        if x[i]<x[i+1]:
            a = 1
            print(a)
        elif x[i]>x[i+1]:
            a = -1
            print(a)
        else:
            a = 0
            print(a)
            

listemiz = [1,3,7,12,6,4,1]
            
        
validMountainArray(listemiz)


                
                
            

            
    