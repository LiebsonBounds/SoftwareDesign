# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 13:10:57 2014

@author: bliebson
"""

a = int(raw_input('a'))
b = int(raw_input('b'))
c = int(raw_input('c'))
n = int(raw_input('n'))

def check_fermat():
    if a**n + b**n == c**n:
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work."
    
print(check_fermat())