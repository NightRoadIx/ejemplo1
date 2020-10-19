# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:25:31 2020

@author: ALEXIS20012
"""

print("algo raro pasa aqui");
datos=int(input("ingrese una cantidas n:"))
#presicion=int(input("ingrese la cantidad presisa que desia ingresar:"))
lista=[]

for tmp in range(1,datos+1,1):
    lista.append(tmp)

for i in range(1,datos+1,1):
    for j in range(1,datos+1,1):
         n=i+j+(2*i*j)
         if(lista.count(n)):
             print(n,"removidos")
             lista.remove(n)
         
x=len(lista)
for i in lista:
    print(i,end=",")