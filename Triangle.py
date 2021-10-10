# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
"""

def classifyTriangle(side_one, side_two, side_three):
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    check_a = isinstance(side_one,int)
    check_b = isinstance(side_two,int)
    check_c = isinstance(side_three,int)
    if not(check_a and check_b and check_c): #moved to top to check types first before making comparisons
        return 'InvalidInput' #removed ;

    # require that the input values be >= 0 and <= 200
    if side_one > 200 or side_two > 200 or side_three > 200:
        return 'InvalidInput'

    if side_one <= 0 or side_two <= 0 or side_three <= 0: #changed b < b to b < 0
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if ((side_one + side_two <= side_three) or (side_one + side_three <= side_two) or (side_two + side_three <= side_one)): #changed logic
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if side_one ==  side_two and side_three == side_one : #added 'c' length check
        return 'Equilateral'
    elif (( side_one ** 2) + (side_two ** 2)) == (side_three ** 2): #changed to square
        return 'Right'
    elif (side_one != side_two) and  (side_two != side_three) and (side_one != side_two):
        return 'Scalene'
    else:
        return 'Isoceles'
