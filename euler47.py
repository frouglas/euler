'''
Created on Aug 20, 2012

The first two consecutive numbers to have two distinct prime factors are:

14 = 2  7
15 = 3  5

The first three consecutive numbers to have three distinct prime factors are:


Find the first four consecutive integers to have four distinct primes 
factors. What is the first of these numbers?

@author: frouglas
'''
import math

def prime(x):
    if x<=1:
        return 0
    j = 2
    while (j<=math.sqrt(x)):
        if x % j == 0:
            return 0
        else:
            if j==2:
                j += 1
                continue
            else:
                j += 2
                continue
    return 1
        


def primefactors(x):
    tempfactors = []
    temppower = []
    if x==1:
        factArray = [tempfactors, temppower]
        return factArray
    j = 2
    tempX = x
    while (j <= math.sqrt(x)):
        if prime(j) == 0:
            j += 2
        while tempX % j == 0:
            try: 
                loc = tempfactors.index(j)
                temppower[loc] += 1
            except ValueError:
                tempfactors.append(j)
                temppower.append(1)
            tempX = tempX / j
        if (prime(int(tempX)) == 1) & (tempX!=x):
            tempfactors.append(int(tempX))
            temppower.append(1)
            break
        if j == 2:
            j += 1
        else:
            j += 2
    factArray = [tempfactors, temppower]
    return factArray

consec = 0
maxConsec = 0
i = 0

while consec < 4:
    i += 1
    if int(i/1000)==i/1000:
        print("checking " + str(i) + "...")
    j = primefactors(i)
    if len(j[0]) != 4:
        consec = 0
        continue
    consec += 1
    if consec > maxConsec:
        maxConsec = consec
        print("string ending in " + str(i) + ", " + str(consec) + " consecutive with 4 factors")
print("the first four consecutive integers to have four distinct prime factors are " + str(i-3) + ", " + str(i-2) + ", " + str(i-1) + ", " + str(i))
