'''
Created on May 18, 2011

A permutation is an ordered arrangement of objects. For example, 3124 
is one possible permutation of the digits 1, 2, 3 and 4. If all of the 
permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

ANSWER: 2783915460

@author: frouglas
'''

import math

dig = []
digCount = []
answer = ""

for i in range(0,10):
    dig.append(i)
    digCount.append(0)
    
iter = 1000000


for i in range(9,0,-1):
    while math.factorial(i) <= iter:
        iter -= math.factorial(i)
        digCount[10 - i] += 1
        
print(digCount)

for i in range(1,10):
    uBound = 1
    for j in digCount[i+1:]:
        if j != 0:
            uBound = 0
            break
    if uBound:
        answer += str(dig[digCount[i]-1])
        dig.pop(digCount[i]-1)
        for k in range(-1,-len(dig)-1,-1):
            answer += str(dig[k])
        break
    else:
        answer += str(dig[digCount[i]])
        dig.pop(digCount[i])
        
print("the 1000000th lexicographic permutation of the digits 0-9 is " + answer)
    
    
    