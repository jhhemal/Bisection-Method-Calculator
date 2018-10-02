#!/usr/bin/python
# Name  :         Python program for implementation 
#                 of Bisection Method 
# 
# Author:         Jahidul Hasan Hemal
# url   :         http://jhhemal.me   
  
from math import *

def func(expr, x):
    return eval(expr)

input_expr = input("f(x) = ")
a = eval(input("Enter a = "))
b = eval(input("Enter b = "))
 
def bisection(a,b): 
  
    if (func(input_expr, a) * func(input_expr, b) >= 0): 
        print("You have not assumed right a and b\n") 
        return
   
    c = a 
    while ((b-a) >= 0.01): 
  
        # Find middle point 
        c = (a+b)/2
   
        # Check if middle point is root 
        if (func(input_expr,c) == 0.0): 
            break
   
        # Decide the side to repeat the steps 
        if (func(input_expr,c)*func(input_expr,a) < 0): 
            b = c 
        else: 
            a = c 
              
    print("The value of root is : ","%.4f"%c) 
      
bisection(a, b) 
  
