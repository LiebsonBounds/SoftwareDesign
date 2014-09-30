# -*- coding: utf-8 -*-
"""

FMyLife Producer

Written by Brian Liebson

Goal of this Program:
Program looks on the random page for FMyLife
Program produces random FML with rankings (how many people "laughed" or "felt" with you)

"""
#get pattern so we can search the interwebs
from pattern.web import *
from random import randint


            
def FML():
    #get entries from FMyLife random page
    random_entries = plaintext(URL('http://www.fmylife.com/random').download())
    
    #creating a list where each entry IN THE LIST is determined by a newline in the page
    entry_list = random_entries.split('\n\n')
    #print entry_list
    #get rid of things that are not entries
    entry_list1 = [x for x in entry_list if x !='This FML has been commented on by its original poster.']
    
    #this part gets rid of extra info on top and bottom
    for i, j in enumerate(entry_list1):
       #find the start of entries
        if 'All the FMLs' in j:
            start_entry = i+1
        #looking for end
        if 'Refresh this page here to get more FMLs!' in j:
            end_entry = i
    #remove content before and after entries
            entry_list1 = entry_list1[start_entry:end_entry] 
            
    entry_list2 = [0,0] #just creating the empty variable to be filled
    #this part removes the Date/Time strings and the comment # strings
    final_list=[]    
    for x in range(4, len(entry_list1)): #starting at 4 cause weird things happen at 0
        if x % 2 == 0:
            entry_list2[2/x] =  entry_list1[x]
            final_list.append(entry_list2[0])
  
  #random number 
    r = randint(0, len(final_list)/2-1)
    return final_list[2*r:2*r+2]    
    #this will make sure the even entry is first so that the FML comes before the rankings
    
print FML()