# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:13:26 2020

@author: ALEXIS20012
"""
m=0

print("Sera Palíndromo mi horacion")
le=0
texto=str(input("ingrese un texto:"))
texto=texto.upper()
lista=list(texto)
listar=list(texto)
listar.reverse()
for tmp in range(0,len(lista)):
    if(lista.count(" ")):
        lista.remove(" ")
for tmp in range(0,len(listar)):
    if(listar.count(" ")):
        listar.remove(" ")

for f in range(0,len(lista)):
    if(lista[f]==listar[f]):
        l=f
    else:
        print(texto,"no es palindromo")
        l=0
        break
if(l>0):
    print(texto,"es palindromo")