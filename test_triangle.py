# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangles(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(12,5,13),'Right','12,5,13 is a Right triangle')
        self.assertEqual(classify_triangle(17,15,8),'Right','17,15,8 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(3,3,3),'Equilateral','3,3,3 should be equilateral')
        self.assertEqual(classify_triangle(100,100,100),'Equilateral','100,100,100 should be equilateral')

    def testIsoscelesTriangles(self): 
        self.assertEqual(classify_triangle(2,2,3),'Isosceles','2,2,3 should be isosceles')
        self.assertEqual(classify_triangle(4,6,4),'Isosceles','4,6,4 should be isosceles')
        self.assertEqual(classify_triangle(30,30,10),'Isosceles','30,30,10 should be isosceles')

    def testScaleneTriangles(self): 
        self.assertEqual(classify_triangle(3,4,6),'Scalene','3,4,6 should be scalene')
        self.assertEqual(classify_triangle(4,8,6),'Scalene','4,8,6 should be scalene')
        self.assertEqual(classify_triangle(30,20,17),'Scalene','30,20,17 should be scalene')

    def testNotTriangles(self): 
        self.assertEqual(classify_triangle(0,1,1),'InvalidInput','0,1,1 should yield invalid input')
        self.assertEqual(classify_triangle(1,0,1),'InvalidInput','1,0,1 should yield invalid input')
        self.assertEqual(classify_triangle(1,1,0),'InvalidInput','1,1,0 should yield invalid input')
        self.assertEqual(classify_triangle('a',1,1),'InvalidInput','a,1,1 should yield invalid input')
        self.assertEqual(classify_triangle(1,'a',1),'InvalidInput','1,a,1 should yield invalid input')
        self.assertEqual(classify_triangle(1,1,'a'),'InvalidInput','1,1,a should yield invalid input')
        self.assertEqual(classify_triangle(5,2,2),'NotATriangle','5,2,2 should yield not a triangle')
        self.assertEqual(classify_triangle(4,8,3),'NotATriangle','4,8,3 should yield not a triangle')
        self.assertEqual(classify_triangle(10,3,7),'NotATriangle','10,3,7 should yield not a triangle')
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

