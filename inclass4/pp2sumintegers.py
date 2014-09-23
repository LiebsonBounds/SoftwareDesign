# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:50:11 2014

@author: bliebson
"""
#this function takes in a range of numbers
#and sums them all together

xinput = int(raw_input('X'))
yinput = int(raw_input('Y'))

def sum_integers():
    sum = 0
    for i in range(xinput, yinput+1):
        sum = sum + i
    return sum
    
print sum_integers()