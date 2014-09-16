# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 10:44:59 2014

@author: bliebson
"""

def two(f):
    f()
    f()
    
def four(f):
    two(f)
    two(f)
    
def print_h_part():
    print '+----',
    
def print_v_part():
    print '|    ',
    
def print_h_full():
    two(print_h_part)
    print '+'
    
def print_v_full():
    two(print_v_part)
    print '|'
    
def print_row():
    print_h_full()
    four(print_v_full)
    
def print_grid():
    two(print_row)
    print_h_full()
    
print_grid()