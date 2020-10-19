# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:36:14 2020

@author: ALEXIS20012
"""
print("de normal a romano")
x=int(input("ingrese un numero:"))
def conversor_entero_roma(entero):
    numeros=[100000,50000,10000,5000,1000,900,500,400,100,90,50,40,10,9,5,4,1];
    numerales=["M'","D'","X'","V'","M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
            
    numeral=""
    i=0
    while entero>0:
        for tpm in range (entero//numeros[i]):
            numeral+=numerales[i]
            entero-=numeros[i]
        i+=1
    return numeral
print(conversor_entero_roma(x))
