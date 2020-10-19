# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:22:35 2020

@author: ALEXIS20012
"""
print("el inversor de numeros")
x=int(input("ingrese un numero:"))
entero= int(x)
#esta formula ayuda ha saber si el valor es entero o fraccionario
b=x-entero
h=int(x)
x=str(x)
r=-1
if (b==0):
    #esta condicion nos ayuda ha asegurar que x solo sea positiva
    while (h>0):

        for t in reversed(x):
            print(t,end=(""))
        break
#cuando a es distinto de cero y menor a 1 esta condicion
#nos dice que el valor es impar
elif(b<1):
    print("error 548wesa")
    print("el numero que ingreso contiene decimal vuelva a intertar otra vez")
#esta condicion ayuda a saber cuando el valor ingresado es negativo 
#o es un valor 0
if(h<0):
    print("error w544es5s")
    print("el numero no es positivo o es cero :( vuelva a intertar otra vez")