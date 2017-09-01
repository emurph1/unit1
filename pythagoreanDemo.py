#Emily Murphy  
#2017-09-01
#pythagoreanDemo.py - how to find hypotenuse with the other two leg lengths (right triangle)

from math import sqrt

a = float(input('Enter leg 1: '))
# : because not a question
b = float(input('Enter leg 2: '))
print('The hypotenuse is', sqrt(a**2 + b**2))

