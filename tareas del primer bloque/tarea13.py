# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:00:34 2020

@author: ALEXIS20012
"""
print("serie de Padovan")
m=0
while(m<1):
    valor=int(input("ingrese el tamaño que desea que se produzca:"))
    if(valor<4):
        for k in range(0,valor,1):
            print("1",end=(","))
    elif(valor<6):
        for k in range(0,3,1):
            print("1",end=(","))
        for k in range(0,valor-3,1):
            print("2",end=(","))
    elif(valor>=6 and valor<101):
        for k in range(0,3,1):
            print("1",end=(","))
        for k in range(0,2,1):
            print("2",end=(","))
        for n in range(4,valor-1,1):
            p=(n-2)+(n-3)
            print(p,end=(","))
    m=int(input("que desea hacer\n0.volver\n1.salir\n:"))
print("que tenga un excelente dia")