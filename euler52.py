'''
Created on Aug 30, 2012

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

@author: frouglas
'''

import copy

from pyFuncs import parse

found = 0
nextX = 0
x = 0

while found==0:
    x += 1
    xDigs = parse(x)
    found = 1
    for i in range(2,7):
        currDigs = parse(i * x)
        digsCopy = copy.copy(xDigs)
        for j in currDigs:
            try:
                loc = digsCopy.index(j)
                removed = digsCopy.pop(loc)
            except ValueError:
                nextX = 1
                found = 0
                break
        if nextX == 1:
            break
        if i == 2:
            print("x = " + str(x))
        print("    " + str(i) + " * " + str(x) + " = " + str(i*x))
    if nextX == 1:
        nextX = 0
        continue
    