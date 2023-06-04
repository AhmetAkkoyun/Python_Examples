# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:35:34 2021

@author: ahmet
"""

#######################
##                   ##
##       Quiz        ##
##  Asal Sayı Bulma  ##
##                   ##
#######################


# Bir Sayının asal olup olmadığını bulan programı yazınız.

print("Merhaba!")
print("Herhangi bir sayının asal olup olmadığını bulabilirim.")





def asalsayibul(x):
    asal=True

    for i in range(2,x):
        if x%i==0 and x!=i:
            asal=False
       
    if asal==False or x==1:
        print(x, "sayısı asal değildir.")
    else:
        print(x, "sayısı asaldır.")


x=int(input("Lütfen bir sayı giriniz: "))
asalsayibul(x)


print("**************************************")


# asal sayıları sırayla yazdırmak

print("Şimdi 1-100 aralığındaki tüm asal sayıları ekrana yazalım")


for x in range(2,100):
    asal=True
    for i in range(2,x):
        if x%i==0 and x!=i:
            asal=False
    if asal==True:
        print(x)
        
        
print("**************************************")

# ilk def ile ne var ne yok yazdırmak

for x in range(1,100):
   asalsayibul(x)        
        
print("**************************************")

            
        

