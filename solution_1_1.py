#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 09:59:46 2018

@author: tdenton
"""

def process_letter(letter):
    if letter.isdigit():
        return(letter)
    if letter.isupper():
        return(letter)
    else:
        pos = ord(letter)-97
        if pos < 0 or pos > 25:
            return letter
        else:
            rev_arry = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
            return(rev_arry[pos])
    
def string_processor(_string):
    final_string = ""
    for letter in _string:
        final_string += process_letter(letter)
    print(final_string)

def answer(s):
    string_processor(s)
