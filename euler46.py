'''
Created on Aug 20, 2012

It was proposed by Christian Goldbach that every odd composite number can 
be written as the sum of a prime and twice a square.

9 = 7 + 212
15 = 7 + 222
21 = 3 + 232
25 = 7 + 232
27 = 19 + 222
33 = 31 + 212

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum 
of a prime and twice a square?

ANSWER: 5777

@author: frouglas
'''
import math
import time



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
    
startTime = time.clock()
    
found = 0
i = 2
primes = []
moveOn = 0

while found==0:
    if prime(i) == 1:
        primes.append(i)
        if (i % 2 == 0):
            i += 1
        else:
            i += 2
        continue
    else:
        for j in range(len(primes),0,-1):
            testI = (i - primes[j-1])/2
            root = math.sqrt(testI)
            if int(root)==root:
                print(str(i) + " = " + str(primes[j-1]) + " + 2 * " + str(int(root)) + "^2")
                i += 2
                moveOn = 1
                break
        if moveOn == 1:
            moveOn = 0
            continue
    found = 1
print("the smallest odd composite is " + str(i))
endTime = time.clock()
elapsedMin = int((endTime - startTime) / 60)
elapsedSec = round((endTime - startTime) - 60*elapsedMin,2)
print("elapsed time: " + str(elapsedMin) + " minutes, " + str(elapsedSec) + " seconds")
    