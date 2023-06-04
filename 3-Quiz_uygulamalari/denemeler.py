# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:06:16 2021

@author: ahmet
"""

def validMountainArray(x):
    i=1    
    while x[i-1]<=x[i]:            
            if x[i+1]<x[i]:
                a = i
                while x[a]>=x[a+1]:
                    if x[a+2]>x[a+1]:                        
                        return False
                    else:
                        return True 
                i=i+1
            i=i+1
        
        
a = [1,0,8,2]  

print(validMountainArray(a))



def validMountainArray(x):
    s = False
    i=1    
    while x[i-1]<=x[i]:
        if x[i+1]<x[i]:
            a = i
            return(a)
        i+1
    while  x[a]>=x[a-1]:
        if x[a-2<x[a-1] or a-1==0:
            while x[a]<=x[a+1]:
                if x[a+2]>[a+1] or a+1==len(x)-1:
                    s = True
                a=a+1
        a=a-1
      
        return(s)
    
            
                
    
    
    

        
a = [1,0,8,2]  

print(validMountainArray(a))

   
    