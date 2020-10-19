# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:46:10 2020
@author: ALEXIS20012
"""
print("Mínimo Común Múltiplo y maximo divisor")
t=int(input("ingrese un valor"))
o=int(input("ingrese otro valor"))
def mcm(x,y):
    z=max(x,y)
    
    while True:
        if(z % x ==0) and (z% y ==0):
            return z
        z+=1
def mcd(x,y):
    mcd=1
    if x % y ==0:
        return
    for k in range(int(y/2),0,-1):
        if x % k==0 and y % k==0:
            mcd = k
            break
    return mcd
print("el minimo comun multiplo es:",mcm(t,o))
print("el maximo comun divisor es:",mcd(t,o))