# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:36:54 2021

@author: ahmet
"""

# faktoryel hesabı yapma 1

def faktoryel(sayi):
    if sayi==1 or sayi==0:
        return 1
    else:
        return sayi * faktoryel(sayi-1)
    
sayinin_faktoryeli= faktoryel(int(input("sayi giriniz: ")))

print("girdiğiniz sayinin faktoryeli: ", sayinin_faktoryeli)


# faktoryel hesabı yapma

def faktoryel(sayi):
    if sayi==1 or sayi==0:
        return 1
    else:
        return sayi * faktoryel(sayi-1)
    
print("girdiğiniz sayinin faktoryeli: ", faktoryel(int(input("lütfen bir sayi giriniz: "))))