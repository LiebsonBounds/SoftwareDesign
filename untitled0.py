# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 16:31:12 2014

@author: bliebson
"""

from random import randint
from math import pi
import Image



def evaluate_random_function(final_function, x, y):
    """ 
    Evaluating the function!
    """
    print eval(final_function)
    
evaluate_random_function("x**2 + y", 40, 8)