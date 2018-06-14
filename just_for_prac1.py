# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 08:18:20 2018
@author: Neetu

This function takes a string named my_string as a parameter and prints the string with enugh leading spaces 
so that the last letter is in column 70 of the display 
"""

def right_justify(my_string):
    r_just_string = ' ' * (70 - len(my_string)) + my_string
    return r_just_string

test_str = "123456789012345678901234567890123456789012345678901234567890"
ret_str = right_justify(test_str)
print("right justified string is ") 
print(ret_str)