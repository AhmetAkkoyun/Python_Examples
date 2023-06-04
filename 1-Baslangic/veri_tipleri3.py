# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:25:56 2021

@author: ahmet
"""

####################
##                ##
##  veri tipleri  ##
##                ##
####################




# dictionary

    #             key   value
mydictionary1 = {"isim":"ali",             # yanyana da yazılabilir          
                "yas":20,                 # ancak düzenli gözükmesi
                "ogrencino":45542343,     # için alt alta tercih
                "sehir":"izmir"           # ediliyor
                }                            
              

mydictionary2 = {"isim":"ayşe",                      
                "yas":23,              
                "ogrencino":43586433,    
                "sehir":"istanbul"         
                }     

mydictionary3 = {"isim":"veli",                   
                "yas":16,               
                "ogrencino":49746563,     
                "sehir":"ankara"          
                }     


print(mydictionary1["isim"])
print(mydictionary1["sehir"])
print(mydictionary2["yas"])
print(mydictionary3["isim"])
print(mydictionary3.get("isim"))   # bir üsttekinin aynısı. alternatif

print(mydictionary1.keys())       # listedeki tüm anahtarları yazar
print(mydictionary1.values())       # listedeki tüm değerleri yazar
print(mydictionary1.items())       # komple listeyi yazar