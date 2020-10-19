# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:42:22 2020

@author: ALEXIS20012
"""
n=int(input("ingrese un valor de la matriz"))
matriza=[[0 for x in range(n)]
        for y in range(n)]
matrizb=[[0 for x in range(n)]
        for y in range(n)]
matriz_suma=[[0 for x in range(n)]
        for y in range(n)]
matriz_resta=[[0 for x in range(n)]
        for y in range(n)]
matriz_multiplicar=[[0 for x in range(n)]
        for y in range(n)]

for i in range(0,n,1):
    for j in range(0,n,1):
        print("ma[",i,"][",j,"]",end="")
        matriza[i][j]=(int(input("ingrese un valor:")))
for i in range(0,n,1):
    for j in range(0,n,1):
        print("mb[",i,"][",j,"]",end="")
        matrizb[i][j]=(int(input("ingrese un valor:")))
        
for i in range(0,n,1):
    for j in range(0,n,1):
        matriz_suma[i][j]=matriza[i][j]+matrizb[i][j]
        matriz_resta[i][j]=matriza[i][j]-matrizb[i][j]    
for i in range(len(matriza)):
    for j in range(len(matrizb[0])):
        for k in range(len(matriza[0])):
            matriz_multiplicar[i][j]+=matriza[i][k]*matrizb[k][j]
print("matriz a orinal")
for j in matriza:
    print(j)
print("matriz b original")
for j in matrizb:
    print(j)
print("matriz suma")
for j in matriz_suma:
    print(j)
print("matriz resta")
for j in matriz_resta:
    print(j)   
print("matriz multiplicacion")
for j in matriz_multiplicar:
    print(j)
print("la determinante de la matriz a y b es",(n-1),"!\n jejejeje\n esto es todo amigos")

        