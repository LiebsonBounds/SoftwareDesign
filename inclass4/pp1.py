# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:18:06 2014

@author: bliebson
"""

# in between function -- takes in (x,y,z)
# returns true iff y iz between x and z

x = int(raw_input('X'))
y = int(raw_input('Y'))
z = int(raw_input('Z'))

def is_between():
    
""" Takes in x, y, and z
If y is between x and z, it will return true
otherwise it returns false
"""

    if y>x:
        if z>y:
            return 'True'
        else:
            return 'False'
    else:
            return 'False'
        
print(is_between())