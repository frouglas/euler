'''
Created on Feb 22, 2016

@author: frouglas


Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d (d^2 + n)/d is prime.

'''

import math
from pyFuncs import *
import numpy
import itertools

counter = 3
print ("    1 is an eligible number")
        
tracker = 3
uLim = 100000000
oddPrimes = [3]
maxProd = 0
escape = 0

while tracker < uLim / 2:
    tracker += 2
    if prime(tracker) == 0:
        continue
#     tracker += 2
#     if prime(tracker)==0:
#         continue
#     counter += 1
#     for i in range(0,len(oddPrimes)):
#         thisInd = i + 1
#         theseFacs = itertools.combinations(oddPrimes,thisInd)
#         for j in theseFacs:
#             thisProd = 2 * numpy.prod(numpy.array(j)) * tracker
#             if thisProd > 100000000:
#                 if thisProd > maxProd:
#                     maxProd = thisProd
#                 escape = 1
#                 break
#             else:
#                 counter += 1
#         if escape == 1:
#             break
#         counter += 1
#     oddPrimes.append(tracker)
#     if len(oddPrimes) % 1000 == 0:
#         print ("checked " + str(len(oddPrimes)) + " primes, highest product found is " + str(maxProd) + ", highest prime checked is " + str(oddPrimes[-1]))
# print str(counter) + " examples found"

print "done!"