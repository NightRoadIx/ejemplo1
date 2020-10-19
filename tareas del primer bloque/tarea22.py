# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:42:39 2020

@author: ALEXIS20012
"""

texto=str(input("ingrese un texto pero no se pase:"))
long=len(texto)
a=A=b=B=C=c=D=d=E=e=F=f=G=g=H=h=I=i=J=j=K=k=L=l=M=m=N=n=Ñ=ñ=O=o=P=p=Q=q=R=r=0
S=s=T=t=U=u=V=v=W=w=X=x=Y=y=Z=z=esp=0
otro=0
for i in range(0,long,1):
    if(texto[i]=="A"):
        A+=1
    elif(texto[i]=="a"):
        a+=1
    elif(texto[i]=="B"):
        B+=1
    elif(texto[i]=="b"):
        b+=1
    elif(texto[i]=="C"):
        C+=1
    elif(texto[i]=="c"):
        c+=1
    elif(texto[i]=="D"):
        D+=1
    elif(texto[i]=="d"):
        d+=1
    elif(texto[i]=="E"):
        E+=1
    elif(texto[i]=="e"):
        e+=1
    elif(texto[i]=="F"):
        F+=1
    elif(texto[i]=="f"):
        f+=1
    elif(texto[i]=="G"):
        G+=1
    elif(texto[i]=="g"):
        g+=1
    elif(texto[i]=="H"):
        H+=1
    elif(texto[i]=="h"):
        h+=1
    elif(texto[i]=="I"):
        I+=1
    elif(texto[i]=="i"):
        i+=1
    elif(texto[i]=="J"):
        J+=1
    elif(texto[i]=="j"):
        j+=1
    elif(texto[i]=="K"):
        K+=1
    elif(texto[i]=="k"):
        k+=1
    elif(texto[i]=="L"):
        L+=1
    elif(texto[i]=="l"):
        l+=1
    elif(texto[i]=="M"):
        M+=1
    elif(texto[i]=="m"):
        m+=1
    elif(texto[i]=="N"):
        N+=1
    elif(texto[i]=="n"):
        n+=1
    elif(texto[i]=="Ñ"):
        Ñ+=1
    elif(texto[i]=="ñ"):
        ñ+=1
    elif(texto[i]=="O"):
        O+=1
    elif(texto[i]=="o"):
        o+=1
    elif(texto[i]=="P"):
        P+=1
    elif(texto[i]=="p"):
        p+=1
    elif(texto[i]=="Q"):
        Q+=1
    elif(texto[i]=="q"):
        q+=1
    elif(texto[i]=="R"):
        R+=1
    elif(texto[i]=="r"):
        r+=1
    elif(texto[i]=="S"):
        S+=1
    elif(texto[i]=="s"):
        s+=1
    elif(texto[i]=="T"):
        T+=1
    elif(texto[i]=="t"):
        t+=1
    elif(texto[i]=="U"):
        U+=1
    elif(texto[i]=="u"):
        u+=1
    elif(texto[i]=="V"):
        V+=1
    elif(texto[i]=="v"):
        v+=1
    elif(texto[i]=="W"):
        W+=1
    elif(texto[i]=="w"):
        w+=1
    elif(texto[i]=="X"):
        X+=1
    elif(texto[i]=="x"):
        x+=1
    elif(texto[i]=="Y"):
        Y+=1
    elif(texto[i]=="y"):
        y+=1
    elif(texto[i]=="Z"):
        Z+=1
    elif(texto[i]=="z"):
        z+=1
    elif(texto[i]==" "):
        esp+=1
    else:
        otro+=1
print("A=",A,"a=",a,"B=",b,"C=",C,"c=",c,"D=",D,"d=",d,"E=",E,"e=",e,"F=",F,"f=",f)
print("G=",G,"g=",g,"H=",H,"h=",h,"I=",I,"i=",i,"J=",J,"j=",j,"K=",K,"k=",k,"L=",L,"l=",l)
print("M=",M,"m=",m,"N=",N,"n=",n,"Ñ=",Ñ,"ñ=",ñ,"O=",O,"o=",o,"P=",P,"p=",p,"Q=",Q,"q=",q)
print("R=",R,"r=",r,"S=",S,"s=",s,"T=",T,"t=",t,"U=",U,"u=",u,"V=",V,"v=",v,"W=",W,"w=",w)
print("X=",X,"x=",x,"Y=",Y,"y=",y,"Z=",Z,"z=",z,"espacios=",esp,"otros caracteres=",otro)





