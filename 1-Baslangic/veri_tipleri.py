# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:16:26 2021

@author: ahmet
"""

####################
##                ##
##  veri tipleri  ##
##                ##
####################



# int str float veri tipleri

a = 5
b = "ahmet"
c = 4.34
d = "5.54"


print(type(a))   # 5 sayısı otomatik int alındı
print(type(b))   # tırnak içi olunca otomaki str oldu
print(type(c))   # ondalıklı olunda otomatik float
print(type(d))   # tırnak içi sayı olsa bile str olur


e = float(d)     # str olan veriyi float olarak çevirme

print(type(e))   # float olarak okundu
print(type(d))   # d değişkeninin veri tipi aynı kaldı


# boolean veri tipi

x = 3 > 5                 # x değerine yanlış bir karşılaştırma atandı

if x == True:
   print("doğru")
else:
    print("yanlış")        # çıktıda else çalıştı ve yanlış dedi


x = 3 < 5                 # x değerine doğru bir karşılaştırma atandı

if x == True:
   print("doğru")
else:
    print("yanlış")       # aynı kod if çalıştırdı ve doğru dedi
    
    
# boolean örnek sayının tek çift olduğunu bulmak

x=int(input("lütfen bir sayı giriniz: "))

if (x%2==1):
    print("tek")
else:
    print("çift")         
    
# şimdi bunu boolean değişkenle yapalım

x=int(input("lütfen bir sayı giriniz: "))

flag_tek = x%2==1 

if flag_tek:
    print("tek")
else:
    print("çift")        # komut aynı şekilde çalışıyor
    
print(type(flag_tek))    # veri tipi bool olarak yazdırıldı.














