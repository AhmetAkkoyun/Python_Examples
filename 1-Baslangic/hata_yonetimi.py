# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:54:53 2021

@author: ahmet
"""

############################
##                        ##
##  Python hata yönetimi  ##
##                        ##
##  Try, Except, Finally  ##
##                        ##
############################
##                        ##
##     Global komutu      ##
##                        ##
############################




# try, except

def bolme_islemi(bolunen,bolen):
    bolum = bolunen / bolen
    return(bolum)

print("*************************************")

# print(bolme_islemi(10,0))  böyle bir işlemde program hata vereceğinden
# print("hoşçakalın")        devam etmeyecek ve hoşçakalın yazmayacaktır.
          
def bolme_islemi2(bolunen,bolen):
    try:
        bolum = bolunen / bolen
        return(bolum)
    except:
        print("bolme isleminde hata bulunmaktadir.")


print(bolme_islemi2(10,0)) # hata mesajımızı yazdı ve sonucu None verdi
print("hoşçakalın")       # ekrana hoşçakalın yazdı

print("*************************************")

# finally
# bu kod genellikle veritabanı ya da socket programlamada kullanılır. 
# işlemin bittiğini ekranda görmek istediğimiz durumlarda işe yarar

def bolme_islemi3(bolunen, bolen):
    try:
        bolum = bolunen / bolen
        return(bolum)
    except:
        print("hatalı veri girişi var bölme işlemi yapılamıyor.")
    finally:
        print("işlem tamamlandı.")

print("*************************************")

# global komutu
# bir fonksiyonun dışardan değer çekmesi için kullanılan komut


islem_no = 0

def toplama(x,y):
    try:
        a=x+y
        islem_no = islem_no + 1       # islem no tanımlı değil
        return(a)                     # bu yüzden hata verecek
    except:
        print("hata var")

    

print(toplama(3,2), "islem no:", islem_no)  
  
print(toplama(5,4), "islem no:", islem_no)

print(toplama(1,1), "islem no:", islem_no)  # islem no hep 0 oldu

print("*************************************")

islem_no = 0

def toplama2(x,y):
    try:
        a=x+y
        global islem_no               # globaldekini kullan dedik
        islem_no = islem_no + 1       # artık tanımlı
        return(a)
    except:
        print("hata var")


print(toplama2(3,2), "islem no:", islem_no)  
  
print(toplama2(5,4), "islem no:", islem_no)

print(toplama2(1,1), "islem no:", islem_no) # işlem no arttırıp verdi



        




    

