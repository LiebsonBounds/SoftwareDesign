# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:23:07 2014

@author: bliebson
"""

# generates a random number in the 
# interval [start, stop]

start = int(raw_input('Start'))
stop = int(raw_input('Stop'))

def random_float():
"""takes in a start and stop values
outputs a random integer within (and including)
those values
"""

    from random import randint
    randomizer = randint(start, stop)
    return randomizer
    
print(random_float())