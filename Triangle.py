# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def is_valid_input(num):
    """Input: any object
    Output: Whether or not num is a proper input for the classify_triangle function"""

    if not isinstance(num, int):
        return False
    if num > 200 or num <= 0:
        return False

    return True

def classify_triangle(side_a, side_b, side_c):
    """Input: int side_a, side_b, side_c, each greater than 0 and less than 201
    Output: String classificiation of the triangle formed by the given sides"""

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(is_valid_input(side_a) and is_valid_input(side_b) and is_valid_input(side_c)):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (side_a >= (side_b + side_c) or
            side_b >= (side_a + side_c) or
            side_c >= (side_a + side_b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if (side_a**2+side_b**2 == side_c**2 or
            side_a**2+side_c**2 == side_b**2 or
            side_b**2+side_c**2 == side_a**2):
        return 'Right'
    if (side_a != side_b) and  (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    return 'Isosceles'
