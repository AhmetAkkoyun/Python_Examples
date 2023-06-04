# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:59:12 2021

@author: ahmet
"""


####################
##                ##
##  veri tipleri  ##
##                ##
####################



# listeler


list = [24, 32, 14, 25, 40]
  #      0   1   2   3   4

print(list[0])        # 24     0 değeri ilk değer
print(list[3])        # 25     
print(list[-1])       # 40     tersten sayınca -1 = 40
print(list[-5])       # 24     -5 değerinden 4 değerine kadar okur diğerleri out of range

print("****************")
print(list[2]+list[3])        # liste içi işlem


list = [24, 32, 14, 25, 40, "izmir", 32.85]

print(list[2]+list[3])        # içerikte str float olunca da aynı işlem yapılabilir

print("****************")

# liste uzunluğu : len komutu listede de çalışır

print(len(list)) 

print("****************")
# listede eleman değiştirme

print(list[4])      # listenin ilk halinde 40 olarak yazacak

list[4] = 3         # 3 olarak değiştirdik

print(list[4])       # 3 olarak yazdırdı.

print("****************")


# tuple - elemanların değiştirilemediği listeler

tuple = (24, 32, 14, 25, 40, "izmir", 32.85)   # aynı liste tuple hali
                                               # parantezler köşeli değil

print(tuple[2])          # işlem yaparken yine köşeli parantez

# tuple[2] = 5       # 14 değerini 5 yapmaya çalışınca hata mesajı verir

tuple = (24, 32, 5, 25, 40, "izmir", 32.85) # değiştirmek istersek tuple 
                                            # listesini baştan tanımla 

print(tuple[2])      # şimdi oldu.