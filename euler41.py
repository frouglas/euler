'''
Created on Aug 18, 2012

We shall say that an n-digit number is pandigital if it makes use 
of all the digits 1 to n exactly once. For example, 2143 is a 4-digit 
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

ANSWER: 7652413

@author: frouglas
'''

import math

def prime(x):
    if x==1:
        return 0
    tempfactors = [1]
    j = 2
    while (j <= math.sqrt(x)) & (len(tempfactors)==1):
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

maxVal = 0
goNext = 0
    
for i in range(1,10):
    currVal = 0
    digits = [0 for j in range(0,i)]
    maxCheck = [0 for j in range(0,i)]
    inUse = [0 for j in range(0,i)]
    init = 1
    check = sum(j for j in range(1,i+1))
    if check % 3 == 0:
        continue
    for j in range(0,i):
        digits[j] = j+1
        inUse[j] = 1
    while maxCheck[0]<i:
        currVal = 0
        j = i
        while j > 0:
            maxCheck[j-1] = digits[j-1]
            if init == 1:
                init = 0
                if (digits[len(digits)-1] % 2 != 0) & (digits[len(digits)-1]!=5):
                    break
            if maxCheck[j-1]==i:
                j -= 1
                continue
            else:
                inUse = [0 for k in range(0,i)]    
                for k in range(0,j-1):
                    inUse[digits[k]-1] = 1
                for k in range(j,i+1):
                    try:
                        newVal = inUse.index(0,maxCheck[k-1]) + 1
                        digits[k-1] = newVal
                        inUse[newVal-1] = 1
                        for l in range(k,i):
                            maxCheck[l] = 0
                    except ValueError:
                        maxCheck[k-1] = i
                        goNext = 1
                        break
                if goNext == 1:
                    j -= 1
                    goNext = 0
                    continue
                elif (digits[len(digits)-1] % 2 == 0) | (digits[len(digits)-1]==5):
                    j = i
                    continue
                else:
                    break
        for j in range(0,i):
                currVal += int(digits[j]*10**(i-j-1))
        if prime(currVal) == 1:
            if currVal > maxVal:
                maxVal = currVal
                print(str(currVal) + " is the largest pandigital prime yet examined")
            
            
    