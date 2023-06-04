# -*- coding: utf-8 -*-


def validMountainArray(x):
    if(len(x)<3):
        return False
    
    # Arrayin yükselen kısmının bittiği noktayı bulalım..
    i = 1
    while(i<len(x) and x[i]>x[i-1]):
        i+=1

    #  Dizinin sonuna geldiysek sadece yükselme işlemi var alçalan kısım yok False döndür..        
    if(i==1 or i==len(x)):
        return False
        
    # Arrayin azalan kismina bakalım nereye kadar azalma olacak
    while(i<len(x) and x[i]<x[i-1]):
        i+=1
        
    # Eğer alçalan kısmın bitişi dizinin sonu ise bu bir Mountain Array'dir..
    # Aksi takdirde tekrar bir yükselme veya eşitlik olacaktır ki Mountain Array tanımına 
    # uymaz...
    if (i==len(x)):
        return True
    else:
        return False


lst = [0,4,5,6,7,10,8,6,5,6,8,9,7,5,3,1]     
print(validMountainArray(lst))
    
