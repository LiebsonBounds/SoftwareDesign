# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:42:18 2014

@author: bliebson
"""


#getting the stuff
from swampy.TurtleWorld import*
world = TurtleWorld()
bob = Turtle()
bob.delay = .5

bob.heading = 0
l = 75

def snow_flake_side():
    """Draw a side of the snowflake curve with side 
    length l and recursion depth of level"""
    bob.fd(l/3)
    bob.heading -=60
    bob.fd(l/3)
    bob.heading +=120
    bob.fd(l/3)
    bob.heading -=60
    bob.fd(l/3)
    
def snow_flake():
    for i in range(3):
        snow_flake_side()
        bob.lt(120)
        
snow_flake()