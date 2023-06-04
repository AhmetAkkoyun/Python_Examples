# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:00:47 2021

@author: ahmet
"""

# verilen sayının faktöryelini bulan program

def faktoryel_bul(x):
    y=1
    while x>0:
        y = y*x
        x = x-1
    return(y)
    
x = int(input("lütfen bir sayı giriniz: "))
print("girdiğiniz sayının faktoryeli: ", faktoryel_bul(x))



# quiz
# echo programı yaz kullanıcı ne yazarsa program geri yazsın
# kullanıcı kapat derse program dursun


def tekrarla(x):
    print(x)

while x!="kapat":
    x=input("bir şeyler yazınız: ")
    tekrarla(x)
    