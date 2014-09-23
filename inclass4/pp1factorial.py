# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:38:43 2014

@author: bliebson
"""

#factorial(n): write a function that returns n!

inputn = int(raw_input('N'))

def factorial(n):
    a=1
    for i in range(1, n+1):
        a = a * i
    return a

print factorial(inputn)