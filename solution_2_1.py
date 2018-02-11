#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:03:24 2018

@author: tdenton
"""
import sys

def answer(xs):
    panel_order = sorted(xs)
    val_array = []
    if len(val_array) == 1:
        return val_array[0]
    
    for index, value in enumerate(panel_order):
        if value != 0:
            if value > 1000:
                val_array.append(1000)
            elif value < -1000:
                val_array.append(-1000)
            else:
                val_array.append(value)
    
    neg_array = []
    pos_array = []
    for x in val_array:
        if x < 0:
            neg_array.append(x)
        elif x > 0:
            pos_array.append(x)
    if len(neg_array) % 2 == 0:
        pass
    else:
        neg_array = neg_array[:-1]
    
    fin_array = (neg_array + pos_array)
    
    if len(fin_array) == 0:
        max_product = 0
    else:
        max_product = 1
    
    for entry in fin_array:
        max_product *= entry
    
    if str(max_product)[-1] == "L":
        return str(max_product)[:-1]
    else:
       return str(max_product)
