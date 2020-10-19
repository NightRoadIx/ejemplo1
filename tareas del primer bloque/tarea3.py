# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:40:22 2020

@author: ALEXIS20012
"""
print("bienvenido a el programa que le va ayudar a saber si un año es  bisiesto")
x=float(input("ingrese un año positivo y mayor a 0= "))
entero= int(x)
#esta formula ayuda ha saber si el valor es entero o fraccionario
b=x-entero
#la primera es a==0 que nos determina si el valor esentero
if (b==0):
    #esta condicion nos ayuda ha asegurar que x solo sea positiva
    while (x>0):
        #d y f determinan si el año ingresado en bisiestro o no
        d=x/100
        f=x/400
        #convierte el valor a entero
        enterod=int(d)
        enterof=int(f)
        #convierte el valor a flotante para que no aya error al momento de 
        #ejecutar la condicion
        l=float(d-enterod)
        o=float(f-enterof)
        #si l como o son 0 el año es bisiestro pero si no el año no es
        #bisiestro
        if (l==0 and o==0):
            print("el año",x,"es bisiesto")
        else:
            print("el año",x,"no es bisiesto")
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
