# -*- coding: utf-8 -*-
"""Lets code Data Structures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l1WkkoiRDe8G5m-cMDICXuGxnmHpPEnh
"""

#Task 1
PI = 3.14
radius = float(input(' Input the radius of a circle: '))
area = PI * radius * radius
print(" Area Of the Circle with radius %f is %f" %(radius,area))

#Task 2
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))