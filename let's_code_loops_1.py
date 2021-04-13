# -*- coding: utf-8 -*-
"""Let's code loops 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_IPkycRVdsoPXZ2Rh71nv6epSmdACu_m

Task 1
"""

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1,end = " ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1