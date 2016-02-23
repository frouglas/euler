'''
Created on Sep 1, 2012

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b  100, what is the maximum digital sum?

@author: frouglas
'''

from pyFuncs import parse

maxSum = 0
currSum = 0

for a in range(1,100):
    for b in range(1,100):
        activeNum = a**b
        digits = parse(activeNum)
        currSum = sum(digits)
        if currSum > maxSum:
            print(str(a) + "**" + str(b) + " has the maximal digital sum, " + str(currSum))
            maxSum = currSum
        
