# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
edited by Brian Liebson


Enjoy


PS This code creates weird random computer-generated art...
...because I can't.
"""

# you do not have to use these particular modules, but they may help
from random import randint
from math import *
from PIL import Image

"""
Assorted Math Functions Below
"""
def prod(a, b):                 #multiplier
    return float(a)*float(b)
def cos_pi(a):                  #cos
    return cos(pi*float(a))
def sin_pi(a):                  #sin
    return sin(pi*float(a))



def build_random_function(min_depth, max_depth):
    """
    Given a minimum depth and a maximum depth (relevant to how nested the function is),
    this will build a random function
    """
    if min_depth == 0 and randint(0,1) == 1:
        xandy = ["x", "y"]                      #stops at minimum depth half the time, Idea taken from Cyprien
        return xandy[randint(0, len(xandy) - 1)]
        
    if max_depth == 1:      
        xandy = ["x", "y"]                      #stops at max depth
        return xandy[randint(0, len(xandy) - 1)]
        
        
    action = ["prod", "cos_pi", "sin_pi"] #starting it off
    
    function = action[randint(0, len(action) - 1)]      #randomly choosing which action to start with
    
    
    if function == "prod":                  #getting all that recursion up in here
        return [function, [build_random_function(min_depth - 1, max_depth - 1)], [build_random_function(min_depth - 1, max_depth - 1)]]
    else:
        return [function, [build_random_function(min_depth - 1, max_depth - 1)]]
        
###THIS IS WORKING NOW
def evaluate_random_function(f, x, y):
    """
    Evaluating the function
    """  
    if f[0] == "x":      #x is x
        return x
    if f[0] == "y":     # y is y
        return y
        
    if f[0] == "prod":      #multiply the terms together
        return prod(evaluate_random_function(f[1][0],x,y), evaluate_random_function(f[2][0],x,y))
    if f[0] == "cos_pi":    #cos
        return cos_pi(evaluate_random_function(f[1][0],x,y))
    if f[0] == "sin_pi":    #sin
        return sin_pi(evaluate_random_function(f[1][0],x,y))

###REMAP_INTERVAL WORKS
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        It's just scaling, it's super easy
    """
    out_diff = float(output_interval_end) - float(output_interval_start)      #difference at end
    in_diff = float(input_interval_end) - float(input_interval_start)         #difference at beginning

    scaler = (float(val) -input_interval_start)/in_diff             #fraction where value is of first interval
    new_val = (scaler * out_diff) + output_interval_start       #scale output by that fraction for new value
    return new_val



"""
Calculating colors
"""
red = build_random_function(7, 10)
green = build_random_function(7, 10)
blue = build_random_function(7, 10)

#Creating the image
img = Image.new("RGB", (350, 350))


#Coloring the pixels
for x in range(0, 349):
    for y in range(0, 349):
        redder = remap_interval(evaluate_random_function(red, remap_interval(x, 0, 349, -1, 1), remap_interval(y, 0, 349, -1, 1)), -1, 1, 0, 255)
        greener = remap_interval(evaluate_random_function(green, remap_interval(x, 0, 349, -1, 1), remap_interval(y, 0, 349, -1, 1)), -1, 1, 0, 255)
        bluer = remap_interval(evaluate_random_function(blue, remap_interval(x, 0, 349, -1, 1), remap_interval(y, 0, 349, -1, 1)), -1, 1, 0, 255)
        img.putpixel((x, y), (int(redder), int(greener), int(bluer)))
        
#Saving the image!
img.save("prettypictures.png", 'PNG')







