# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:07:00 2020

@author: ALEXIS20012
"""
a=0
while (a<1):
    texto=str(input("ingrsese un texto no mayor a 100 caracteres:"))
    f=len(texto)
    lista=texto.split()
    long=len(lista)
    if(f<101):
        for i in range(long,0,-1):
            print(lista[0:i])
    else:
        print("su cadena es de",f,"el cual supera los 100 caracteres\n")
    a=int(input("ingrese 0 para regresar\n1 para salir\n:"))