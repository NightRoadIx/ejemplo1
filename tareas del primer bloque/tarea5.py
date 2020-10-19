# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:55:29 2020

@author: ALEXIS20012
"""
print("TRIANGULO DE PASCAL")
x=int(input("ingrese el tamaño maximo de pascal:"))
y=int(input("ingrese el valor de inicio:"))
def pascal (filas):
    fila=[y]
    inicio=[0]
    for i in range(filas):
        print(fila)
        fila = [i+d for i , d in zip(fila +inicio,inicio + fila)]
pascal(x)