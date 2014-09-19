# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 10:44:59 2014

@author: bliebson
"""
a = int(raw_input('Size of Grid'))

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
    
def print_h_full2():
    two(print_h_part)
    print '+'
    
def print_h_full4():
    four(print_h_part)
    print '+'
    
def print_v_full2():
    two(print_v_part)
    print '|'
    
def print_v_full4():
    four(print_v_part)
    print '|'
    
def print_row2():
    print_h_full2()
    four(print_v_full2)
    
def print_row4():
    print_h_full4()
    four(print_v_full4)
    
def print_grid2():
    two(print_row2)
    print_h_full2()
    
def print_grid4():
    four(print_row4)
    print_h_full4()
    
if a == 2:
    print_grid2()
    
if a == 4:
    print_grid4()
    
