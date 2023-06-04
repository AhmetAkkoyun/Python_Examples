# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:31:27 2021

@author: ahmet
"""

# hesap makinesi 1

def toplama(a,b):
    return(a+b)

def cikarma(a,b):
    return(a-b)
   
def carpma(a,b):
    return(a*b)

def bolme(a,b):
    return(a/b)

a=int(input("lütfen işlem yapmak istediğiniz ilk sayiyi giriniz: "))
x=input("lütfen yapmak istediğiniz işlemi seçiniz (+,-,*,/): ")
b=int(input("lütfen işlem yapmak istediğiniz ikinci sayiyi giriniz: "))

if x=="+":
   c=toplama(a,b)
   print(a,"+",b,"=",c)
       
elif x=="-":
     c=cikarma(a,b)
     print(a,"-",b,"=",c)
         
elif x=="*":
     c=carpma(a,b)
     print(a,"*",b,"=",c)
         
elif x=="/":
     c=bolme(a,b)
     print(a,"/",b,"=",c)
         
else:
     print("işlem yapılamadı. lütfen dört işlem işaretinden birini seçerek tekrar deneyiniz",)    

