# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:56:34 2020

@author: ALEXIS20012
"""
from string import ascii_lowercase , ascii_uppercase

def cifrado_cesar(texto,pasitos):
    texto_resultante=[]
    
    for c in texto:
        if c in ascii_lowercase:
            indice=ascii_lowercase.index(c)
            nuevo_indice=(indice + pasitos)% len(ascii_lowercase)
            texto_resultante.append(ascii_lowercase[nuevo_indice])
        elif c in ascii_uppercase:
            indice=ascii_uppercase.index(c)
            nuevo_indice=(indice + pasitos)% len(ascii_uppercase)
            texto_resultante.append(ascii_uppercase[nuevo_indice])
        else:
            texto_resultante.append(c)
    return ''.join(texto_resultante)
texto=str(input("ingrese un texto:"))
pasitos=int(input("ingrese la candidad de pasos a desifrar:"))
if pasitos<=100:
    for tmp in range(1,pasitos+1,1):
        print("ronda",tmp,":",cifrado_cesar(texto,tmp))