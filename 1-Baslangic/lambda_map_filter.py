# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:53:28 2021

@author: ahmet
"""

###########################
##                       ##
##  Lambda, Map, Filter  ##
##                       ##
###########################


mylist = [1, 2, 3, 4, 5]

# bu listenin tüm elemanlarının küpünü for ile alalım

def kupunu_al(x):
    return(x**3)

for item in mylist:
    print(kupunu_al(item))       # sırayla ekrana yazar

print("****************************")

# şimdi kupunu_al fonksiyonunu kullanarak map ile aynı işlemi yapalım 

yeni_list = list(map(kupunu_al, mylist))      # map başına list belirt

print(yeni_list)                # liste olarak ekrana yazar      

print("****************************")


# lambda kullanımı - kolay fonk yazmaya yarar

lambda sayi: sayi**3      # def gibi ama anlık fonk yazmak gerekirse


yeni_list2= list(map(lambda a: a**3, yeni_list))

print(yeni_list2)            # aynı işlem ama yukardan def çağırmadık


print("****************************")


# filter 

# tek sayıları filtreleyelim


def tek_bul(x):
    if x%2==1:
        return(x)
        
        
yeni_list5 = (list(map(tek_bul, mylist)))

print(yeni_list5)                # çiftleri none yaparak yeni list verdi.


# şimdi aynısını filter ile yap


yeni_list6 = (list(filter(tek_bul, mylist)))

print(yeni_list6)                 # none olanları da ayıkladı.


           


