# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(12,5,13),'Right','12,5,13 is a Right triangle')
        self.assertEqual(classifyTriangle(17,15,8),'Right','17,15,8 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be equilateral')
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 should be equilateral')

    def testIsoscelesTriangles(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 should be isosceles')
        self.assertEqual(classifyTriangle(4,6,4),'Isoceles','4,6,4 should be isosceles')
        self.assertEqual(classifyTriangle(30,30,10),'Equilateral','30,30,10 should be isosceles')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 should be scalene')
        self.assertEqual(classifyTriangle(4,8,6),'Scalene','4,8,6 should be scalene')
        self.assertEqual(classifyTriangle(30,20,17),'Equilateral','30,20,17 should be scalene')

    def testNotTriangles(self): 
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','0,1,1 should yield invalid input')
        self.assertEqual(classifyTriangle(1,0,1),'InvalidInput','1,0,1 should yield invalid input')
        self.assertEqual(classifyTriangle(1,1,0),'InvalidInput','1,1,0 should yield invalid input')
        self.assertEqual(classifyTriangle('a',1,1),'InvalidInput','a,1,1 should yield invalid input')
        self.assertEqual(classifyTriangle(1,'a',1),'InvalidInput','1,a,1 should yield invalid input')
        self.assertEqual(classifyTriangle(1,1,'a'),'InvalidInput','1,1,a should yield invalid input')
        self.assertEqual(classifyTriangle(5,2,2),'NotATriangle','5,2,2 should yield not a triangle')
        self.assertEqual(classifyTriangle(4,8,3),'NotATriangle','4,8,3 should yield not a triangle')
        self.assertEqual(classifyTriangle(10,3,7),'NotATriangle','10,3,7 should yield not a triangle')
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

