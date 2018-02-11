#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:29:04 2018

@author: tdenton
"""
from fractions import Fraction, gcd

#markov chain

def transpose(matrix):
    height = len(matrix)
    if len(matrix) == 0:
        return(matrix)
    width = len(matrix[0])
    new_matrix = []
    for y in range(0, width):
        new_row = []
        for x in range(0,height):
            new_row.append(matrix[x][y])
        new_matrix.append(new_row)
    return new_matrix
    
#multiply oddly
def multiply_matrix(matr_a, matr_b):
    inv_b = transpose(matr_b)
    
    final_array = []
    
    for y in inv_b:
        temp_row = []
        for x in matr_a:
            total = 0
            for index, x_x in enumerate(x):
                total += y[index]*x_x
            temp_row.append(total)
        final_array.append(temp_row)
    final_array = transpose(final_array)
    return(final_array[0])

#Not original work
def invert(matrix):
    n = len(matrix)
    inverse = [[Fraction(0) for col in range(n)] for row in range(n)]
    for i in range(n):
        inverse[i][i] = Fraction(1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][i] == 0:
                    return False
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(n):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    for i in range(n):
        a = matrix[i][i]
        if a == 0:
            return False
        for j in range(n):
            inverse[i][j] = inverse[i][j] / a
    return inverse
#####################
    
def subtractBase(matr_a, matr_b):
    new_matrix = []
    # Turn Matrix into fractions
    for x, row in enumerate(matr_a):
        for y, value in enumerate(row):
            matr_a[x][y] = Fraction(value, 1)
            
    for x, row in enumerate(matr_a):
        new_row = []
        for y, value in enumerate(row):
            new_row.append(value - matr_b[x][y])
        new_matrix.append(new_row)
    return(new_matrix)        

def format_matrix(array_list, matrix):
    counter = []
    
    for x in range(0,len(jim)):
        counter.append(x)
    for x in array_list:
        counter.remove(x)
    
    x_range = array_list + counter
    fin_matrix = []
    for x in x_range:
        temp_array = []
        for y in x_range:
            temp_array.append(matrix[x][y])
        fin_matrix.append(temp_array)    
    return x_range, fin_matrix

def find_fr(num, matrix):
    size_fr = len(matrix) - num
    tempfr = matrix[-size_fr:]
    fr = []
    for row in tempfr:
        fr.append(row[:num])
    return fr
    
def find_i(num, matrix):
    size_i = len(matrix) - num
    i = []
    for x in range(0,size_i):
        tempArry = [0] * size_i
        tempArry[x] = 1
        i.append(tempArry)
    return i
    
def find_q(num, matrix):
    size_q = len(matrix) - num
    tempq = matrix[-size_q:]
    q = []
    for row in tempq:
        q.append(row[-size_q:])
    return q

def find_z(num, matrix):
    size_z = len(matrix) - num
    tempz = matrix[:num]
    z = []
    for row in tempz:
        z.append(row[-size_z:])
    return z

def _lcm(array):
    frac_array = []
    for value in array:
        frac_array.append([value.numerator, value.denominator])
        
    num_den = transpose(frac_array)
    dens = sorted(list(set(num_den[1])))
    for item in dens:
        if item == 1:
            dens.remove(1)
            
    #not original but modified
    lcm = dens[0]
    for i in dens[1:]:
      lcm = lcm*i/gcd(lcm, i)
    ############################
    
    return_array = []
    
    for value in frac_array:
        return_array.append(value[0]* (lcm/value[1]))
    return_array.append(lcm)
    return(return_array)
    
def answer(state_array):
    global jim 
    jim = state_array
    # Find terminal
    final = []
    un_final = []
    if len(state_array) == 1:
        return([1,1])
    for index, x in enumerate(jim):
        f_final = False
        if all(y == 0 for y in x):
            final.append(index)
            f_final = True
            
        #this finds final states that are hidden by 1
        if f_final == False:
            if sum(x) == x[index]:
                final.append(index)

    
    for entry in final:
        found = False
        for row in jim:
            for index, x in enumerate(row):
                if x != 0 and x != sum(jim[index]):
                    if index == entry:
                        found = True
        if found == False:
            un_final.append(entry)
       
    # set initial ending
    final_lst = [None] * (len(final) + 1)
    
    if len(un_final) > 0:
        for index, entry in enumerate(final):
            if entry in un_final:
                #print(entry, index)
                final_lst[index] = 0

    #fill in values with 1s
    for value in final:
        jim[value][value] = 1

    #transform matrix into standard form
    x_range, matrix = format_matrix(final, jim)    

    i = find_i(len(final), matrix)
    z = find_z(len(final), matrix)
    fr = find_fr(len(final), matrix)
    q = find_q(len(final), matrix)
    
    denominators = []
    for row in matrix:
        denominators.append(sum(row))
    denominators = denominators[-len(fr):]
    
    # Add denominators to q
    for index, den in enumerate(denominators):
        for y, x in enumerate(q[index]):
            q[index][y] = Fraction(x,den)
        
    # Add denominators to FR
    for index, den in enumerate(denominators):
        for y, x in enumerate(fr[index]):
            fr[index][y] = Fraction(x,den)
    
    #Subract Matricies
    I_Q = subtractBase(i, q)
    
    F = invert(I_Q)
    
    finArray = multiply_matrix(F, fr)
    fin = _lcm(finArray)
    return(fin)
