# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:33:11 2020

@author: ALEXIS20012
"""

print("sumador de digitos")
entrada=int(input("ingrese un valor:"))
f=str(entrada)
long=len(f)
g=entrada
suma=0
while(long>0):
    y=g/(pow(10,long-1))
    b=int(y)
    u=b*(pow(10,long-1))
    suma=suma+b

    if (long==1):
        print(b,"=",suma)
        break
    print(b,end="+")
    g=g-u
    long=long-1
    