# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:50:15 2020

@author: ALEXIS20012
"""

print("bienvenido a la multiplicadora")
x=float(input("ingrese un valor entero y positivo a multiplicar: "))
entero= int(x)
#esta formula ayuda ha saber si el valor es entero o fraccionario
b=x-entero
#la primera es a==0 que nos determina si el valor esentero
if (b==0):
    #esta condicion nos ayuda ha asegurar que x solo sea positiva
    while (x>0):
        for k in range(1, 11, 1):
            #multiplica la funcion
            a=x*k
            print("|",x,"X",k,"=",a,"|")
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