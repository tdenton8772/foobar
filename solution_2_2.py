#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:17:33 2018

@author: tdenton
"""

def answer(pegs):
    _max = pegs[1] - pegs[0] - 1
    for firstGear in range(1, _max):
        gears = [firstGear]
        for index, peg in enumerate(pegs):
            if index ==0:
                pass
            else:
                gears.append(pegs[index] - (pegs[index-1] + gears[-1]))
        if any(gear <= 0 for gear in gears):
            continue

        if firstGear == 2 * gears[-1]:
            return [firstGear, 1]

        if firstGear+1 == 2 * gears[-1]:
            return [(firstGear * 3) + 1, 3]
        
        if firstGear+2 == 2 * gears[-1]:
            return [(firstGear * 3) + 2, 3]

    return [-1, -1]
