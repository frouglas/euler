'''
Created on Aug 30, 2012

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =    
n!
r!(nr)!
,where r  n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?

@author: frouglas

'''

import math

from pyFuncs import comb

counter = 0
skip = 0

for i in range(1,101):
    if i % 2 == 0:
        uLim = int(i / 2)
    else:
        uLim = int(i/2) + 1
    for j in range(uLim,0,-1):
        if skip == 1:
            skip = 0
            continue
        combVal = comb(i,j)
        if combVal>1000000:
            print(str(i) + " choose " + str(j) + " = " + str(combVal))
            counter += 1
            if i - j != j:
                print(str(i) + " choose " + str(i - j) + " = " + str(combVal))
                counter += 1
                if 2*j-i == 1:
                    skip = 1
        else:
            break
print("there are " + str(counter) + " values of n C r greater than 1000000")

