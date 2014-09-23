# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 13:49:13 2014

@author: bliebson
"""

# this is a function which takes an input n 
# and returns a value twice the value of n
n = int(raw_input('Enter a number to be doubled and square rooted.'))

def double():
    b = n*2
    return b
    
print(double())

# this is a function that computes the
# square root of a number

def mysqrt():
    c = n**0.5
    return c
    
print(mysqrt())