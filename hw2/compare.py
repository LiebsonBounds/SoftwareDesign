# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 12:56:51 2014

@author: bliebson
"""

x = int(raw_input('X'))
y = int(raw_input('Y'))

def compare():
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

print(compare())
