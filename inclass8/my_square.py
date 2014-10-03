# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 13:49:03 2014

@author: bliebson

Goal of function is to take an input of the coordinates 
of the lower lefthand corner and the side length of a
square and draws the square to the Turtle world canvas
"""

#getting the stuff
from swampy.TurtleWorld import*
world = TurtleWorld()
bob = Turtle()


def my_regular_polygon():
    xcoordinate = input('Enter x coordinate')   #enter coordinates
    ycoordinate = input('Enter y coordinate')
    length = input('Enter side length')
    sides = 4
        
    for x in range(1, sides):
        bob.heading = x * 360 / sides
        bob.fd(length)
        
my_regular_polygon()