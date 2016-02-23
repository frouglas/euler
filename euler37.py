'''
Created on Aug 16, 2012

@author: frouglas
'''

import math

def parse(inStr):
    inStr = str(inStr)
    temp = []
    for i in range(0,len(inStr)):
        temp.append(int(inStr[i]))
    return temp

def rtrunc(num):
    num = str(num)
    num = num[0:len(num)-1]
    num = int(num)
    return num

def ltrunc(num):
    num = str(num)
    num = num[1:len(num)]
    num = int(num)
    return num

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

i = 11
found = 0
checked = [1,2,3,5,7]
primes = [0,1,1,1,1]
truncPrimes = [0,0,0,0,0]
skipForward = 0
holla = 0
skipCycle = 0
runSum = 0

while found<11:
    if (i % 10000 == 1):
        print("checked through " + str(i-1) + ", truncatable primes found: " + str(found))
    truncPrime = 1
    digits = parse(i)
    for j in range(len(digits)-1,-1,-1):
        if ((digits[j]==1) & ((j==0) | (j==len(digits)-1))):
            digits[j] += 1
        while ((digits[j] % 2 == 0) | (digits[j]==5) | (digits[j]==0)):
            if ((digits[j]==2) | (digits[j] == 5)):
                if (j==0):
                    break
            skipForward = 1
            digits[j] += 1
        if skipForward == 1:
            for k in range(j+1,len(digits)):
                digits[k] = 1
            break
    if skipForward == 1:
        if holla == 1:
            holla =1
        newI = 0
        for j in range(0,len(digits)):
            newI += digits[j]*10**(len(digits)-j-1)
        if (newI % 2 == 0):
            newI += 1
        i = newI
        skipForward = 0
        continue
    if skipCycle==1:
        skipCycle=0
        continue
    iPrime = prime(i)
    checked.append(i)
    primes.append(iPrime)
    if iPrime == 1:
        if holla == 1:
            holla = 1
        rTrunc = 1
        rSkip = 0
        lTrunc = 1
        lSkip = 0
        rTru = i
        lTru = i
        for j in range(0,len(str(i))-1):
            if rSkip ==0:
                rTru = rtrunc(rTru)
                try:
                    loc = checked.index(rTru)
                    if truncPrimes[loc]==1:
                        rskip = 1
                    elif (primes[loc]==1):
                        rSkip = 0
                    else:
                        rTrunc = 0
                        break
                except ValueError:
                    primeTru = prime(rTru)
                    checked.append(rTru)
                    primes.append(primeTru)
                    truncPrimes.append(0)
                    if primeTru==0:
                        rTrunc = 0
                        break
            if lSkip ==0:
                lTru = ltrunc(lTru)
                try:
                    loc = checked.index(lTru)
                    if (truncPrimes[loc]==1):
                        lskip = 1
                    elif (primes[loc]==1):
                        lskip = 0
                    else:
                        lTrunc = 0
                        break
                except ValueError:
                    primeTru = prime(lTru)
                    checked.append(lTru)
                    primes.append(primeTru)
                    truncPrimes.append(0)
                    if primeTru==0:
                        lTrunc = 0
                        break
    else:
        rTrunc=0
    if (lTrunc==1 & rTrunc == 1):
        truncPrimes.append(1)
        found += 1
        runSum += i
        print(str(i) + " is a truncatable prime, total found = " + str(found) + ", running sum: " + str(runSum))
    else:
        truncPrimes.append(0)
    i += 2
            