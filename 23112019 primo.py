# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 23:00:23 2018

@author: Christyan
"""

#in portuguese tempo means time
from time import perf_counter as tempo

#Enter an integer between 0 and infinite lol! Python has all integer precision we need!
#eval is insecure, but I need to evaluate Mersenne Prime expressions like 2**31-1
#I would protect it more, filtering only Natural integers above 0...
n = eval(input("Enter an integer number:"))

#in portuguese primo means prime I won't change it!
#Catches if number is even, smaller than 2 or a perfect square
primo = (((n&1) and (n>2)) or (n==2)) and (n**0.5 != int(n**0.5))

#in portuguese limite means limit i could ignore upper limit as n and go to square root of n...
limite = range(3,n,2)

#in portuguese inicio means start
#just a time counter efficiency measurements...
inicio = tempo()

#if less or equals 2 means composite or prime if 2, loop isn't necessary...
if (primo) and (n>2):
    
    for i in limite:
        
        primo = n%i
        
        #anyway won't count to n! if prime or composite        
        if (i*i>n) or (not primo):
                   
            break
        
print("This is a Prime number!" if primo else "This is a Composite number!","Elapsed time in seconds:",tempo()-inicio)
print("This integer is a perfect square!" if (n**0.5) == int(n**0.5) else "",end = "")
