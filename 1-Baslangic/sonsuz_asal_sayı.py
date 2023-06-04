# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:02:52 2021

@author: ahmet
"""

print("Şimdi sonsuza kadar tüm asal sayıları ekrana yazalım")

x=1
y=2
while x+1>x and x<5:                      # and ve sonrası kalkarsa sonsuz
    x=x+1
    for x in range(x,x+1):
        asal=True
        for i in range(2,x):
            if x%i==0 and x!=i:
                asal=False
    
        if asal==True:
            print(x)

  
            
   
        