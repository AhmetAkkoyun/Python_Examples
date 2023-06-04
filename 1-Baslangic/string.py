# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:09:09 2021

@author: ahmet
"""

# string kullanımları

mystring= "MERHABA"
print(mystring)

print(len(mystring))   # string uzunluğunu verir

print(mystring[0])     # herhangi bir sıradaki karakteri verir. 
                       # python da sıralam 0 dan başlar.

print(mystring[3])     # 0=M 1=E 2=R 3=H


# HABA yazdır
print(mystring[3:])

# ER yazdır
print(mystring[1:3])

# ABA yazdır
print(mystring[4:])
print(mystring[4:7])

# MER yazdır
print(mystring[:3])
print(mystring[0:3])

# MRA yazdır
print(mystring[0:5:2])   #ikinci : kaçar tane atlayacağını gösterir



#string birleştirme 

str1= "merhaba"
str2= "dünya"
str3= str1 + str2
print(str3)

#merhabadünya arasına boşluk için " " kullanabiliriz

str3= str1 + " " + str2
print(str3)


#büyük küçük harf değiştirme 

str1= "merhaba dünya"
str1buyut= str1.upper()   #yanına .upper() ekleyince harfler büyür
str1kucult= str1buyut.lower()  #yanına .lower() ekleyince harfler küçülür

print(str1)
print(str1buyut)
print(str1kucult)

# string ayırma

str1 = "merhaba dünya"
print(str1.split())  # kelimeleri ayıran komut


# virgül kullanılan yerlerde ayırma
str1 = "merhaba,dünya,tüm,çocuklar,güzeldir."
print(str1.split())            #olmadı çünkü tek kelime sanıyor

print(str1.split(","))         #şimdi oldu.
