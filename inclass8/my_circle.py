# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:14:59 2014

@author: bliebson

This takes an input of the center and radius of a circle 
then draws the circle to the canvas by approximating
the circle as a regular polygon of a large number of sides
"""

#getting the stuff
from swampy.TurtleWorld import*
from math import*
world = TurtleWorld()
bob = Turtle()
bob.delay = .0001
def my_regular_polygon():
    xcoordinate = input('Enter x coordinate')   #enter coordinates
    ycoordinate = input('Enter y coordinate')
    radius = input('Enter radius')
    
    #randomly saying number of sides = 2 * radius
    sides = 5*radius
    length = 2 * pi * radius / sides
        

    for x in range(1, sides):
        bob.heading = x * 360 / sides
        bob.fd(length)
        
my_regular_polygon()
        