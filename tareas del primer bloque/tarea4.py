# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:11:59 2020

@author: ALEXIS20012
"""
#(i+1)en print sirve pasa sumar
#(i+1)*"hola" nos dice cuantas veces va a aparecer hola en una linea
#cuando usamos la resta para reducir
##(i*1)*"hola" aqui se reduce las lineas. ejemplo si al inicio tenemos 4 holas en una linea
#al imprimir la siguiente linea va hacer 3 holas y asi hasta llegar a 0 o al numero minimo 
#que asignamos
print("bienvenido a el creador de figuras")
print("ADVERTENCIA AL MOMENTO DE ELEGIR LA FIGURA SOLO PONGA UN CARACTER")
print("selecione el tipo de figura")
print("1.para genera una piramide 90°")
print("2.para genera una medio diamante")
print("3.para genera una diamante")
print("4.para genera una piramide")
print("5.para genera una piramide invertida")
print("6.para genera una piramide 90° invertido")
opcion=int(input("que opcion elige:"))

if opcion==1:
   #ingresa el tamaño de la piramire
   tamano=int(input("ingrese el tamaño de la figura: "))
   #elige la figura que decias que se imprima
   figura=str(input("elija la figura: "))
   i=1
   #nos ayuda a saber cual es el tamaño maximo de la figura
   j=tamano-1
   #imprime la figura
   while i<tamano:
    print((i)*(figura))
    j=j-1
    i=i+1
elif opcion==2:
   tamano=int(input("ingrese el tamaño de la figura: "))
   figura=str(input("elija la figura: "))
   i=0
   #da el tamaño maximo
   j=tamano
   #imprime la primera figura
   while i<=tamano:
    print((i+1)*(figura))
#la misma figura pero invertida
    while j<=tamano & i==tamano:
       print((tamano-j)*(figura))
       j=j+1
        
    j=j-1
    i=i+1
elif opcion==3:
   tamano=int(input("ingrese el tamaño de la figura: "))
   figura=str(input("elija la figura: "))
   i=1
   j=tamano
   while i<=tamano:
    print((j*' ')+(i)*(figura)+(i-1)*(figura))
    while j<=tamano & i==tamano:
     print(((j+1)*' ')+(tamano-j)*(figura)+(tamano-j-1)*(figura))
     j=j+1
    j=j-1
    i=i+1
elif opcion==4:
   tamano=int(input("ingrese el tamaño de la figura: "))
   figura=str(input("elija la figura: "))
   i=1
   j=tamano
   while i<=tamano:
    print((j*' ')+(i)*(figura)+(i-1)*(figura)) 
    j=j-1
    i=i+1
elif opcion==5:
    tamano=int(input("ingrese el tamaño de la figura: "))
    figura=str(input("elija la figura: "))
    i=tamano
    j=1
    while j<=tamano & i==tamano:
     print(((j+1)*' ')+(tamano-j)*(figura)+(tamano-j-1)*(figura))
     j=j+1 
elif opcion==6:
    tamano=int(input("ingrese el tamaño de la figura: "))
    figura=str(input("elija la figura: "))
    i=tamano+1
    j=0
    while j<=tamano:
     print((i-1)*(figura))
     i=i-1
     j=j+1
else:
 print("por aqui no era")

