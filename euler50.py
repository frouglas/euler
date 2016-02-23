'''
Created on Aug 25, 2012

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

@author: frouglas
'''
import copy

from pyFuncs import prime

bigPrimes = []

maxCons = 0
maxSum = 0
primeSums = [2]
runSum = 2
i = 3
cont = 1

while cont==1:
    if int((i-1)/1000) == (i-1)/1000:
        print(str(i-1))
    if prime(i) == 1:
        runSum += i
        primeSums.append(runSum)
        if runSum < 1000000:
            if (prime(runSum)==1):
                maxCons = runSum
                maxSum = len(primeSums)
                print(str(maxCons) + " is the greatest sum of consecutive primes, the sum of " + str(maxSum) + " primes")
            else:
                pSums = copy.copy(primeSums)
                while len(pSums)>=maxSum+2:
                    subt = pSums.pop(0)
                    tempSum = runSum - subt
                    if prime(tempSum)==1:
                        maxCons = tempSum
                        maxSum = len(pSums)
                        print(str(maxCons) + " is the greatest sum of consecutive primes, the sum of " + str(maxSum) + " primes")                       
    if runSum-primeSums[len(primeSums)-maxSum]>1000000:
        print(str(primeSums[len(primeSums)-maxSum]))
        break
    i += 2
    


