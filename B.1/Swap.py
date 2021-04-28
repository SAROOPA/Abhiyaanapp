#!/usr/bin/env python

import math
def Calc_swaps(n_1):
    fix= math.ceil(n_1/2) - 1
    print("Psition of Fixed element :" ,pos[fix])
    s=0
    for i in range (0,n_1):
        s = s + abs(pos[fix]-pos[i]) - abs(fix-i)
    print("Minimum number of swaps : " ,s)    
        
    
def Min_swaps(a,n):
    n_1=0
    global pos
    pos = []
    for i in range(0,n):
        if(a[i]==1):
            n_1= n_1 + 1
            pos.append(i)
    print("Number of ones :", n_1)
    print("Position of ones :" , pos)
    Calc_swaps(n_1)        
            
            
a=[]
n=int(input("Enter the number of elements"))
print("Enter the elements")
for i in range(0,n):
    a.append(int(input()))
Min_swaps(a,n)  




