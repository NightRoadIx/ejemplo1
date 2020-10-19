# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:45:42 2020

@author: ALEXIS20012
"""

print("calculadora de la doble factorial (n!!)")
#ingresa los valores del usuario
x=float(input("Ingresa un valor entero y postivo de: "))
#convierte el valor flotante a un valor entero 
#y porque flotante pues por una sencilla razon y es que evita que el
#programa de error al momento de ingresar los datos
entero= int(x)
#esta formula ayuda ha saber si el valor es entero o fraccionario
a=x-entero
factorial=1
n=x
n=int(n)
#como lo hace aqui tenemos 3 condiciones: 
#la primera es a==0 que nos determina que el valor es entero
if (a==0):
    #esta condicion nos ayuda ha asegurar que x solo sea positiva
   while (x>0):
     #esta funcion nos ayuda a determinar si el valor es impar
     # o es par
     y=x
     y=y/2
     #ase lo mismo que al inicio pero con la diferencia que ahorra 
     #nos ayuda a saber si es par o impar
     enterob=int(y)
     b=y-enterob
     #si el valor es 0 es par pero si el valor es distinto de 0 es impar
     if b==0:
         y=int(x)
         while (n>1):
             factorial=factorial*n
             if(n==2):
              print("la doble factorial de",y,"es",factorial)
             n=n-2
     else:
       y=int(x)
       while (n>0):
             factorial=factorial*n
             if(n==1):
              print("la doble factorial de",y,"es",factorial)
             n=n-2   
     break
  
#cuando a es distinto de cero y menor a 1 esta condicion
#nos dice que el valor es impar
elif(a<1):
    print("error 489FKS#$")
    print("el numero que ingreso contiene decimal vuelva a intertar otra vez")
#esta condicion ayuda a saber cuando el valor ingresado es negativo 
#o es un valor 0
if(x<=0):
    print("error EIISH546")
    print("el numero no es positivo o es cero :( vuelva a intertar otra vez")

print("gracias por usa la app =)")