# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:11:06 2020

@author: ALEXIS20012
"""
print("generador de numeros")
a=int(input("ingrese el primer valor a:"))
b=int(input("ingrese un valor b:"))
m=int(input("ingrese la cantidad del modulo:"))
N=int(input("ingrese el tamaño que decea general:"))
n=0
x=[a]
un=[]
print('|{:3}|\t|{:2}|\t\t|{:12}|\t|{:4}|'.format("n","Xn","Xn+1=(aXn+b)%m","Un=Xn/m"))
while (n<N):
    
    un.append(x[n]/m)
    x.append((a*x[n]+b)%m)
    print("|{:3}|\t|{:2}|\t\t|({:}*{:}+{:})mod{:}={:}|\t|{:4}|".format(n,x[n],a,x[n],b,m,x[n+1],round(un[n],4)))
    n+=1
    
"""n=0

print("n",end=" ")
for tmp in (lista_n):
    print("{:6}\t".format("tmp"))
print("")
print("xn",end=" ")
for tmp in (lista_xn):
    print(tmp,end=(" "))
print("")
print("un",end=" ")
for tmp in (lista_un):
    print((tmp),end=" ")
    """
    
    
    
    
    
    
print("\n este es un mensaje perturbador")