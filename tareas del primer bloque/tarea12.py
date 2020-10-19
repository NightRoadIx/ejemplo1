# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:33:50 2020

@author: ALEXIS20012
"""

print("conversor a EEE 754-1985")
entradad=float(input("ingrese el valor:"))
lista_decimales=[]
lista_fraciones=[]
lista_exponente=[]
if (entradad>0):
    signo=0
else:
    signo=1
    entradad=entradad*-1
decimal=int(entradad)
fraccion=entradad-decimal
while (decimal>0):
    y=decimal/2
     #ase lo mismo que al inicio pero con la diferencia que ahorra 
     #nos ayuda a saber si es par o impar
    enterob=int(y)
    b=y-enterob
     #si el valor es 0 es par pero si el valor es distinto de 0 es impar
    if b==0:
    #para valores pares   
        lista_decimales.append(0)  
    
    else:
      #para valores impreres
        lista_decimales.append(1)
    decimal=decimal/2
    decimal=int(decimal)
    #calcula la longitud decimal del valor
long=len(lista_decimales)
if(decimal==0):
    lista_fraciones.append(0)
while(fraccion<1 and fraccion>0):
    fraccion=fraccion*2
    if(fraccion>=1):
        lista_fraciones.append(1)
        break
    lista_fraciones.append(0)
#calcula la longitud de la lista de fracion
longf=len(lista_fraciones)
recorrido=127+(long-1)
while (recorrido>0):
    y=recorrido/2
     #ase lo mismo que al inicio pero con la diferencia que ahorra 
     #nos ayuda a saber si es par o impar
    enterob=int(y)
    b=y-enterob
     #si el valor es 0 es par pero si el valor es distinto de 0 es impar
    if b==0:
    #para valores pares   
        lista_exponente.append(0)  
    
    else:
      #para valores impreres
        lista_exponente.append(1)
    recorrido=recorrido/2
    recorrido=int(recorrido)
#longitud para lo 23 bit
longt=23-(long+longf)
#imprime el valor del signo
print("signo de 1 bit\n[",signo,"]")
print("si el valor es 0 es positivo y 1 es negativo")
#imprime lo que vale la exponencial
print("exponencial de 8 bits")
print("| ",end="")
#invierta la lista ya que esta invertida
for tmp in reversed(lista_exponente):
    print(tmp,end=" ")
print("|")
# coloca la mantiza
print("mantiza 23 bits")
print("| ",end="")
for (tmp) in reversed(lista_decimales):
    print(tmp,end=" ")
for tmp in (lista_fraciones):
    print(tmp,end=" ")
print((longt)*"0 "+"|")
print(2*"\n")

print("matriz original")
print("|",signo*"-",end="")
for tmp in reversed(lista_decimales):
    print(tmp,end=" ")
print(".",end="")
for tmp in (lista_fraciones):
    print(tmp,end=" ")
print("|")





