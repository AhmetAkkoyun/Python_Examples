# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:50:01 2021

@author: ahmet
"""

#####################
##                 ##
##  Random Modulu  ##
##                 ##
#####################

# random modulu

import random     

# 0 ile 1 arasında rastgele bir sayı üretelim

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())    # her seferinde farklı sayı üretir



print("*************************************************************")

# 2 sayı arasında rastgele bir sayı üretelim 

print(random.uniform(10,20))
print(random.uniform(10,20))
print(random.uniform(20,10))   # sayıların sırası önemli değil



print("*************************************************************")

# 2 sayı arasında rastgele tamsayı üretelim

print(random.randint(10,20))
print(random.randint(10,20))
print(random.randint(10,20))
print(random.randint(10,20))



print("*************************************************************")

# farklı bir yöntem daha var

print(*range(10))  # bu komut 10 a kadar olan sayıları yazdıran komut

print("*************************************************************")

print(random.choice(range(10)))
print(random.choice(range(10)))
print(random.choice(range(10)))   # içinden seç yazdır dedik



print("*************************************************************")

# 0 dan 99 a kadar olan sayılardan rastgele 5 rakam seçtirelim

print(random.sample(range(100), k=5))

# farklı adetlerde seçtirelim

print(random.sample(range(100), k=2))
print(random.sample(range(100), k=7))
print(random.sample(range(100), k=4))



print("*************************************************************")

# range komutu ile ilgili

x = range(10)
print(type(x))     # bu dizinin sınıfı range olarak görünür


x1 = list(range(10))
print(type(x1))       # bu şekilde list yapabiliriz



print("*************************************************************")

# random komutu ile bir listeyi karıştırma


mylist  = [1, 2, 4, 8, 9, 11, 23, 36, 420]

print(mylist)     # verdiğimiz sırayla yazdı

random.shuffle(mylist)

print(mylist)      # listenin karıştırılmış hali yazıldı


yenilist = random.shuffle(mylist)
print(yenilist)                     # none verir çünkü shuffle return yapmaz



print("*************************************************************")