# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:12:05 2020

@author: ALEXIS20012
"""
print("calculadora de números de Keith")
x=int(input("ingrese un valor:"))
entero= int(x)
long=len(str(x))

#esta formula ayuda ha saber si el valor es entero o fraccionario
b=x-entero
g=x
lista=[]
#la primera es a==0 que nos determina si el valor esentero
if (b==0):
    #esta condicion nos ayuda ha asegurar que x solo sea positiva
    while (x>=100):
        while(long>0):
            y=g/(pow(10,long-1))
            b=int(y)
            lista.append(str(b))
            u=b*(pow(10,long-1))
            g=int(g-u)
            long=long-1
        n=0
        suma=0
        while(suma<=x):
            suma=int(lista[n])+int(lista[n+1])+int(lista[n+2])
            lista.append(str(suma))
            n=n+1
            if(suma==x):
                print("el valor es un número de Keith")
                break
            elif(suma>x):
                print("el numero no es de keiyh")
                break
        break
#cuando a es distinto de cero y menor a 1 esta condicion
#nos dice que el valor es impar
elif(b<1):
    print("error 548wesa")
    print("el numero que ingreso contiene decimal vuelva a intertar otra vez")
#esta condicion ayuda a saber cuando el valor ingresado es negativo 
#o es un valor 0
if(x<100):
    print("error w544es5s")
    print("el numero es menor a 100 :( vuelva a intertar otra vez")