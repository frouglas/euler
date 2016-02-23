'''
Created on Aug 7, 2012

Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values 
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible 
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  was discovered, which 
produces 80 primes for the consecutive values n = 0 to 79. The product of the 
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that 
produces the maximum number of primes for consecutive values of n, starting with 
n = 0.

ANSWER: -59231

@author: frouglas
'''

import random
import math

def prime(x):
    tempfactors = [1]
    j = 2
    while j <= math.sqrt(x):
        if x % j == 0:
            if j > tempfactors[len(tempfactors)-1]:
                    tempfactors.append(j)
            else:
                    tempfactors.append(0)
                    k = len(tempfactors)-2
                    while j < tempfactors[k]:
                        tempfactors[k+1]=tempfactors[k]
                        k -= 1
                    tempfactors[k+1]=j
            if x / j != j:
                if x / j > tempfactors[len(tempfactors)-1]:
                    tempfactors.append(int(x/j))
                else:
                    tempfactors.append(0)
                    k = len(tempfactors)-2
                    while int(x/j) < tempfactors[k]:
                        tempfactors[k+1]=tempfactors[k]
                        k -= 1
                    tempfactors[k+1]=int(x/j)
        j += 1
    if len(tempfactors)==1:
        return 1
    else:
        return 0

uBound = int(input("set upper limit for a and b: "))
uBound += 1
maxCons = 0
maxA = 0
maxB = 0
for a in range(-uBound+1,uBound):
    for b in range(1, uBound): 
        contBool = 1
        startPt = 0
        if prime(b)==0:
            continue
        else:
            while (contBool):
                testNum = startPt**2 + a*startPt + b
                if testNum <= 0:
                    break
                if prime(testNum):
                    if startPt>maxCons:
                        maxCons = startPt
                        print("current streak: 0 to " + str(maxCons) + ", a = " + str(a) + ", b = " + str(b))
                        maxA = a
                        maxB = b
                    startPt += 1
                else:
                    contBool=0
    if a/100 == int(a/100):
        print("through " + str(a) + ". . .")
      
prod = maxA*maxB  
print("the maximum consecutively generated primes is " + str(maxCons) + " with a = " + str(maxA) + " and b = " + str(maxB))
print("the product of a and b is " + str(prod))
    
                    