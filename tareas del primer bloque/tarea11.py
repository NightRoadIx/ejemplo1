# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:30:55 2020

@author: ALEXIS20012
"""
print("generador de codigo de barra")
print("ADVERTENCIA el codigo no debe ser mayor a 8")
codigo=str(input("ingrese su codigo de barras\n"))
longitud=len(codigo)
sumai=0
sumap=0
if(longitud<9):
    for j in range(0,longitud,2):
        valor1=codigo[j]
        primeras=int(valor1)
        sumai=sumai+primeras
    for k in range(1,longitud,2):
        valor2=codigo[k]
        segunda=int(valor2)
        sumap=sumap+segunda
    sumap=sumap*3
    sumares=sumai+sumap
    residuo=sumares/10
    residuox=int(residuo)
    conversor=(residuo-residuox)*10
    valorrestante=10-conversor
    valorrestante=int(valorrestante)
    print("el codigo final es")
    print((longitud+3)*"|")
    print(codigo,valorrestante)
else:
    print("el cogigo super los 8 digitos")
    