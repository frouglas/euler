'''
Created on Aug 16, 2012

The number, 197, is called a circular prime because all rotations 
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 
31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

@author: frouglas
'''

import random
import math


def parse(inStr):
    temp = []
    for i in range(0,len(inStr)):
        temp.append(int(inStr[i]))
    return temp

def rotate(num):
    numStr = str(num)
    newStr = ""
    for i in range(0,len(numStr)):
        newStr = newStr + numStr[(i+1)%len(numStr)]
    newStr = int(newStr)
    return newStr

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

found = 4
checked = [2,3,5,7]
checkedPrime = [1,1,1,1]
circlePrime = [1,1,1,1]

for i in range(11,1000000,2):
    digits = parse(str(i))
    circPrime = 1
    for j in digits:
        if ((j % 2 == 0) | (j==5) | (j==0)):
            circPrime = 0
            break
    if circPrime == 0:
        continue
    activeNum = i
    for j in range(0, len(digits)):
        try:
            loc = checked.index(activeNum)
            if checkedPrime[loc] == 1:
                if circlePrime[loc] == 1:
                    break
                if j < len(digits)-1:
                    activeNum = rotate(activeNum)
                continue
            else:
                circPrime = 0
                break
            continue
        except ValueError:
            activePrime = prime(activeNum)
            checked.append(activeNum)
            checkedPrime.append(activePrime)
            circlePrime.append(0)
            if activePrime==1:
                if j < len(digits)-1:
                    activeNum = rotate(activeNum)
                continue
            else:
                circPrime = 0 
                break
    if circPrime == 1:
        found += 1
        circlePrime[checked.index(i)] = 1
        print(str(i) + " is a circular prime, total found = " + str(found))
        
print("total circular primes below 1,000,000: " + str(found))
                
            