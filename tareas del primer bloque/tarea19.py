# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:35:38 2020

@author: ALEXIS20012
"""
print("maquina para encontra π/4 usando la Fracción continua")
n=float(input("ingrese el tamaño de la variable:"))
n=int(n)
sum=1
i=n
while i!=0:
    sum=(2*i-1)+(i**2)/sum
    i-=1
print("π/4 con",n,"términos es:",sum)
