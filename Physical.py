#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fizik:  
   

    def __init__(self):
        self.g=9.8
        self.v0=0
        self.v=0
        self.t=0
        self.h=0
        self.m=0
        
    
    def BirinciFormul(self):
        if self.t != None:
            return self.g * self.t
   
    def IkinciFormul(self):
        if self.v0 != None and self.t != None:
            return 1/2 * (self.g*self.t*self.t) 
        
        
    def Potansiyel(self):
        if self.m != None and self.h != None:
            return self.m * self.g * self.h    
        
    
    def Kinetik(self):
        if self.m != None and self.v != None:
            return 1 / 2 *  self.m *  self.v *  self.v
        
    
    def Toplam(self):
        if  self.m != None and  self.v != None and  self.h != None:
            return  self.m *  self.g *  self.h + 1/2 *  self.m *  self.v *  self.v        
        
    
    def BirinciSecim(self):         
        
        sayi2 =self.t= int(input("t = "))
        sayi3 =self.h= input("H değerini aramak istiyorsanız h: \nV değerini aramak istiyorsanız v: \n ")
        
        if sayi3 == 'v':
            print("v = ",self.g,"*",sayi2,"=",self.BirinciFormul())
        elif sayi3 == 'h':
            print("h= ",1/2,"*",f"{self.g * sayi2 * sayi2}","= {}".format(self.IkinciFormul()))
       
         
    def IkinciSecim(self):
        sayi1 =self.m= int(input("m = "))
        sayi2 =self.h=int(input("h = "))
        if sayi1 != None and sayi2 != None:
            print("Ep = ",sayi1 ,"*",self.g,"*",sayi2,"= ",self.Potansiyel())
      
    def UcuncuSecim(self):
        sayi1 =self.m= int(input("m = "))
        sayi2 =self.v= int(input("v = "))
        if sayi1 != None and sayi2 != None:
            print("Ek= ",1/2,sayi1,"*",sayi2,"*",sayi2,"= ",self.Kinetik())
    
    def DorduncuSecim(self):
        sayi1 =self.m=int(input("m = "))
        sayi2 =self.v= int(input("v = "))
        sayi3 =self.h= int(input("h = "))
        if sayi1 != None and sayi2 !=None and sayi3 != None:
            print("Em = ",sayi1,"*",self.g,"*",sayi3,"+",1/2,sayi1,"*",sayi2,"*",sayi2,"= ",Toplam())

A=Fizik()

while True:   
    print("-" * 115)
    print("Fizik problemleri çözen programa hoşgeldiniz")
    print("")
    secim = input("Potansiyel enerji hesaplamak için: 2 \nSerbest düşmeyi hesaplama için:  1 \nKinetik enerjiyi Hesaplamak için: 3 \nMekanik Enerji Hesaplamak için: 4 \n  ")
    if secim == '1':
        secim1 = A.BirinciSecim()
    elif secim == '2':
        secim1 = A.IkinciSecim()
    elif secim == '3':
        secim1 = A.UcuncuSecim()
    elif secim == '4':
        secim1 = A.DorduncuSecim()
    else:
        print("Devam edilecek bir program.")
        break


# In[ ]:





# 

# In[ ]:





# In[ ]:





# In[ ]:




