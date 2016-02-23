'''
Created on Aug 20, 2012

The arithmetic sequence, 1487, 4817, 8147, in which each of the 
terms increases by 3330, is unusual in two ways: (i) each of the three 
terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit 
primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

@author: frouglas
'''

import math

def parse(x):
    inStr = str(x)
    temp = []
    for i in range(0,len(inStr)):
        temp.append(int(inStr[i]))
    return temp

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

dq = 0
nextI = 0
found = 0
checked= []
active = []

for i in range(1001,10001,2):
    if i == 2969:
        holla = 1
    if prime(i) == 0:
        checked.append(i)
        active.append(1)
        continue
    digits = parse(i)
    firstI = 1
    diffs = []
    anaPrimes = []
    if active != []:
        active = [0 for j in range(0,len(checked))]
    for k in range(0,4):
        for l in range(0,4):
            if l==k:
                continue
            for m in range(0,4):
                if (m==3) & (k==1) & (l==2):
                    holla = 1
                if (m==l) | (m==k):
                    continue
                for n in range(0,4):
                    if (n==m) | (n==l) | (n==k):
                        continue
                    if (digits[k] == 0) | (digits[n] % 2 == 0):
                        continue
                    actNum = str(digits[k]) + str(digits[l]) + str(digits[m]) + str(digits[n])
                    intNum = int(actNum)
                    checked.append(intNum)
                    active.append(1)
                    if prime(intNum)==0:
                        #print("**not prime**")
                        continue
                    elif intNum==i:
                        #print("**i**")
                        continue
                    else:
                        if firstI == 1:
                            #print("i = " + str(i))
                            firstI = 0
                        diff = intNum - i
                        if i % 2 == 0:
                            newNum = int((i + intNum)/2)
                            if prime(newNum) == 1:
                                tempDigs = parse(newNum)
                                iDigs = parse(i)
                                dq = 0
                                for z in range(0,4):
                                    if z==2:
                                        holla = 1
                                    try:
                                        iDigs.remove(tempDigs[z])                                            
                                    except ValueError:
                                        dq = 1
                                        break                                            
                                if dq == 0:
                                    print(str(i) + ", " + str(newNum) + ", " + str(intNum))
                                    found += 1
                                    nextI = 1
                        newNum = int(2*intNum - i)
                        if (prime(newNum)==1) & (len(str(newNum))==4):
                            tempDigs = parse(newNum)
                            iDigs = parse(i)
                            dq = 0
                            for z in range(0,4):
                                if z==2:
                                    holla = 1
                                try:
                                    iDigs.remove(tempDigs[z])
                                except ValueError:
                                    dq = 1
                                    break                                            
                            if dq == 0:
                                print(str(i) + ", " + str(intNum) + ", " + str(newNum))
                                found += 1
                                nextI = 1
                                break
                        newNum = 2*i-intNum
                        if newNum < i:
                            continue
                        if (prime(newNum) == 1)  & (len(str(newNum))==4):
                            tempDigs = parse(newNum)
                            iDigs = parse(i)
                            dq = 0
                            for z in range(0,4):
                                if z==2:
                                    holla = 1
                                try:
                                    iDigs.remove(tempDigs[z])
                                except ValueError:
                                    dq = 1
                                    break                                            
                            if dq == 0:
                                print(str(newNum) + ", " + str(i) + ", " + str(intNum))
                                found += 1
                                nextI = 1
                if (nextI == 1):
                    break
            if nextI == 1:
                break
        if nextI == 1:
            nextI = 0
            break
    if found==2:
        break