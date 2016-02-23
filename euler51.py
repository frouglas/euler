'''
Created on Aug 30, 2012

@author: frouglas
'''
'''
Created on Aug 25, 2012

By replacing the 1st digit of *3, it turns out that six of the nine 
possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among 
the ten generated numbers, yielding the family: 56003, 56113, 56333, 
56443, 56663, 56773, and 56993. Consequently 56003, being the first 
member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight 
prime value family.

@author: frouglas
'''
import copy

from pyFuncs import prime, parse, unparse

famSize = 0
maxFamSize = 0
i = 9
checked = []
repDig = []
primeFam = []
firstDig = 0
lLim = 0
complete = 0

while famSize < 8:
    i += 2
    if (int((i-1)/10000)==(i-1)/10000):
        print("checking " + str(i-1) + " . . .")
    if i == 56003:
        holla = 1
    if prime(i)==1:
        digits = parse(i)
        for j in range(1,len(digits)):
            repDig = [k for k in range(0,j)]
            while(repDig[0]<len(digits)-len(repDig)):
                currCheck = ""
                primeFam = []
                firstDig = 0
                for k in range(0,len(digits)):
                    try:
                        loc = repDig.index(k)
                        if k == 0:
                            firstDig = 1
                        currCheck += "*"
                    except ValueError:
                        currCheck += str(digits[k])
                try:
                    loc = checked.index(currCheck)
                except ValueError:
                    checked.append(currCheck)
                    if firstDig == 1:
                        lLim = 1
                    else:
                        lLim = 0
                    digCopy = copy.copy(digits)
                    for l in range(lLim, 10):
                        if len(primeFam) + 10 - l < maxFamSize:
                            break
                        if (l % 2 == 0) & repDig[len(repDig)-1]==len(digits)-1:
                            continue
                        for m in repDig:
                            digCopy[m] = l
                        activeVal = unparse(digCopy)
                        if prime(activeVal)==1:
                            primeFam.append(activeVal)
                    if len(primeFam) > maxFamSize:
                        print(currCheck)
                        counter = 1
                        for l in primeFam:
                            print("    " + str(counter) + ": " + str(l))
                            counter += 1
                        maxFamSize = len(primeFam)
                if maxFamSize == 8:
                    break
                for l in range(len(repDig)-1,-1,-1):
                    if (repDig[l]==len(digits)-(len(repDig)-1-l)):
                        continue
                    repDig[l] += 1
                    if repDig[l] == len(digits)-1:
                        if l == 0:
                            repDig[l] += 1
                        continue
                    adder = 1
                    for m in range(l+1,len(repDig)):
                        repDig[m] = repDig[l] + adder
                        adder += 1
                    break
            if maxFamSize == 8:
                break            