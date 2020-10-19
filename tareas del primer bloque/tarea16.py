# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:11:20 2020

@author: ALEXIS20012
"""
x=int(input("ingrese un valor:"))
entero= int(x)
#esta formula ayuda ha saber si el valor es entero o fraccionario
b=x-entero
#la primera es a==0 que nos determina si el valor esentero
if (b==0):
    #esta condicion nos ayuda ha asegurar que x solo sea positiva
    while (x>0):
        def narcisistas(n):
            for i in range (0,n+1):
                m=len(str(i))
                s=0
                for digitos in str(i):
                    s+=int (digitos)**m
                if(s==i):
                    print(i)
        print(narcisistas(x))
        break
#cuando a es distinto de cero y menor a 1 esta condicion
#nos dice que el valor es impar
elif(b<1):
    print("error 548wesa")
    print("el numero que ingreso contiene decimal vuelva a intertar otra vez")
#esta condicion ayuda a saber cuando el valor ingresado es negativo 
#o es un valor 0
if(x<=0):
    print("error w544es5s")
    print("el numero no es positivo o es cero :( vuelva a intertar otra vez")