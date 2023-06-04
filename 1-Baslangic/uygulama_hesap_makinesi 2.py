# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:31:27 2021

@author: ahmet
"""

# hesap makinesi 2

a=int(input("lütfen işlem yapmak istediğiniz ilk sayiyi giriniz: "))
x=input("lütfen yapmak istediğiniz işlemi seçiniz (+,-,*,/): ")
b=int(input("lütfen işlem yapmak istediğiniz ikinci sayiyi giriniz: "))


def hesapla(a,b,x):
    
        if x=="+":
           return(a+b,x)
            
        elif x=="-":
             return(a-b,x)
            
        elif x=="*":
             return(a*b,x)
            
        elif x=="/":
             return(a/b,x)
            
        else:
            print("")
            print(x, "geçerli bir işlem değil!")
            x=input("lütfen sadece +, -, * veya / işaretlerinden birini giriniz: ")
            return(hesapla(a,b,x))
            
            
c,x =hesapla(a,b,x)
print(a,x,b,"=",c)        

    
        