# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:01:03 2014

@author: bliebson

This takes the input of the lower lefthand vertex, 
the side length, and the number of sides of a regular
polygon and draws the polygon to the Turtle world canvas
"""

#getting the stuff
from swampy.TurtleWorld import*
world = TurtleWorld()
bob = Turtle()

def my_regular_polygon():
    xcoordinate = input('Enter x coordinate')   #enter coordinates
    ycoordinate = input('Enter y coordinate')
    length = input('Enter side length')
    sides = input('Enter number of sides')
    if sides <= 2:
        print "IMPOSSIBLE!!!!"
        

    for x in range(1, sides):
        bob.heading = x * 360 / sides
        bob.fd(length)
        
my_regular_polygon()
        