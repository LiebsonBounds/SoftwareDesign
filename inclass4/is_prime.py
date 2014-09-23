# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:56:32 2014

@author: bliebson
"""

#is_prime(n): write a function that returns
#True iff n is a prime number

prime = int(raw_input())

def is_prime():
    prime
    for i in range(2, prime):
        remainder = prime % i
        if remainder == 0:
            return 'False'
        else:
            return 'True'
            
print is_prime()