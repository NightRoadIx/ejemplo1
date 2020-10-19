# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:54:10 2020

@author: ALEXIS20012
"""
print("bienvenido a el programa que le suma y da un producto")
menu=0
while (menu<1):
    x=float(input("ingrese el primer valor"))
    y=float(input("ingrese el segundo valor"))
    entero= int(x)
    enteroy=int(y)
#esta formula ayuda ha saber si el valor es entero o fraccionario
    b=x-entero
    c=y-enteroy
#la primera es a==0 que nos determina si el valor esentero
    if (b==0 and c==0) :
    #esta condicion nos ayuda ha asegurar que x solo sea positivo
        while (x>0 and y>0):
            x=int(x)
            y=int(y)
        
        
            if(x<y):
                suma=x
                suma=suma+x
                mult=pow(x,2)
                for k in range(x,y+1,1):
                    print("producto es")
                    print("|",x,"+",k,"=",suma,"|")
                    print("|",x,"*",k,"=",mult,"|")
                    mult=x*(k+1)
                    suma=suma+1
                break
            elif(x>y):
                   suma=x
                   suma=suma+(y)
                   mult=x*(y)
                   for k in range (y,x+1,1):
                       print("producto es")
                       print("|",x,"+",k,"=",suma,"|")
                       print("|",x,"*",k,"=",mult,"|")
                       mult=x*(k+1)
                       suma=suma+1 
                   break
            elif(x==y):
                suma=x+y
                mult=x*y
                print("producto es")
                print("|",x,"+",y,"=",suma,"|")
                print("|",x,"*",y,"=",mult,"|")
                break
            else:
                print("a ocurrido un error inprevisto")
                break
        
#cuando a es distinto de cero y menor a 1 esta condicion
#nos dice que el valor es impar
    elif(b<1 and c<1):
        print("error 548wesa")
        print("el numero que ingreso contiene decimal vuelva a intertar otra vez")
#esta condicion ayuda a saber cuando el valor ingresado es negativo 
#o es un valor 0

    if(x<0 or y<0):
        print("error w544es5s")
        print("el numero no es positivo o es cero :( vuelva a intertar otra vez")
    
    menu=int(input("0.meter otros valores \n1.salir\n..."))