#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:09:49 2019

@author: me
"""

import concurrent.futures
import time

#primo means prime in portuguese
#numero, inicio, fim means number, start, finish in portuguese
def primo(numero,inicio,fim):
    
    i = inicio
    
    #eprimo means isprime in portuguese
    eprimo = not numero % i == 0
    
    while (eprimo) and (i <= fim):
        
        eprimo = not numero % i == 0
        
        i += 2

    return eprimo
            
n=eval(input("Enter an integer number:"))

if (n&1) and (n>3) and (n**0.5 != int(n**0.5)):
    
    #conta means count used as number of threads, tasks
    conta=eval(input("Tasks:"))
    
    start = time.perf_counter()
    
    #raiz means square root of n in portuguese
    raiz = int(n**0.5)

    if raiz&1:
    
        raiz += 1
    
    raiz += 1
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        
        i = 3
        
        secs = []
        
        #here I break the task in "conta" slices        
        for j in range(conta):
            
            if (j+1)*int(raiz/conta)&1:
                secs.append([n,i,(j+1)*int(raiz/conta)])
            else:
                secs.append([n,i,(j+1)*int(raiz/conta)+1])
                
            if (j+1) == conta:
                secs[j] = [n,i,raiz]
                
            i = (j+1)*int(raiz/conta) + 2
            
            if not i&1:
                i += 1
                
        print(secs)
        
        results = executor.map(primo, *zip(*secs))
        
        #lista means list in portuguese
        lista = list(results)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
    print(f'Finished in {(finish-start)//60} minute(s)')
    #if False in lista, in some point numero%i was zero, so the number
    #isn't prime with more than two divisors
    print('Composite' if False in lista else 'Prime')
    print(lista)

else:
    
    print('Prime' if (n == 2) or (n == 3) else 'Composite')
