# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:05:27 2020

@author: ALEXIS20012
"""
print("conversor de numeros a multiplicador x10")
x=int(input("ingrese un numero "))
t=str(x)
longitud=len(t)
u=x
while (longitud>0):
    
    g=u/(pow(10,longitud-1))
    h=int(g)
    h=h*(pow(10,longitud-1))
    if(longitud==1):
        print(h,("="),x)
        break
   # print(h,"\n+")
    print(h, end="+")
    h=int(h)
    u=u-h
    longitud=longitud-1