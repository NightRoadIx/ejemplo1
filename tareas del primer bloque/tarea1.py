# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:34:49 2020

@author: ALEXIS20012
"""

'''caja magica que predice si es par o impar'''
print("bienvenido al la caja magina")
#ingreso de datos por el usuario
x=float(input("Ingresa un valor entero y postivo de: "))
#convierte el valor flotante a un valor entero 
#y porque flotante pues por una sencilla razon y es que evita que el
#programa de error al momento de ingresar los datos
entero= int(x)
#esta formula ayuda ha saber si el valor es entero o fraccionario
a=x-entero
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
       print("el numero %d es par" %x)
       break
     else:
       print("el numero %d es impar"%x)
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