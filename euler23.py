'''
Created on August 6, 2012

@author: frouglas

Problem 23: A perfect number is a number for which the sum of its proper divisors is exactly equal 
to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called 
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be 
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that 
all integers greater than 28123 can be written as the sum of two abundant numbers. However, this 
upper limit cannot be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Answer: 4,179,871 (20,161 is the largest number that cannot be written as the sum of two abundant numbers)
'''
import random
import math

def divisor(x):
    tempdivisors = [1]
    j = 2
    while j <= math.sqrt(x):
        if x % j == 0:
            if j > tempdivisors[len(tempdivisors)-1]:
                    tempdivisors.append(j)
            else:
                    tempdivisors.append(0)
                    k = len(tempdivisors)-2
                    while j < tempdivisors[k]:
                        tempdivisors[k+1]=tempdivisors[k]
                        k -= 1
                    tempdivisors[k+1]=j
            if x / j != j:
                if x / j > tempdivisors[len(tempdivisors)-1]:
                    tempdivisors.append(int(x/j))
                else:
                    tempdivisors.append(0)
                    k = len(tempdivisors)-2
                    while int(x/j) < tempdivisors[k]:
                        tempdivisors[k+1]=tempdivisors[k]
                        k -= 1
                    tempdivisors[k+1]=int(x/j)
        j += 1
    return tempdivisors

uBound = int(input('specify upper bound for analysis: '))
upperLim = min(2*uBound,28123)
abundant = [0 for i in range(0,uBound)]
sumAbundant = [0 for i in range(0,upperLim)]
runTot = 0

for i in range(1,uBound+1):
    divs = divisor(i)
    divSum = 0
    for j in divs:
        divSum += j
    if divSum > i:
        abundant[i-1] = 1
        for j in range(1,i+1):
            if abundant[j-1]==1:
                if i+j < upperLim+1:
                    sumAbundant[i+j-1]=1
    stop = 1
    highest = i
    if 2 * i >= upperLim:
        k = upperLim - 1
        while k > i:
            if sumAbundant[k]==0:
                stop = 0
                break
            k -= 1
    else:
        stop = 0
    if stop:
        print("all candidates found, summing...")
        break
    if (i) % 500 == 0:
        print(str(i) + " completed ...")
        
for i in range(1,upperLim+1):
    if sumAbundant[i-1]==0:
        runTot += i

print("the sum of all numbers that can't be expressed as the sum of two abundant numbers is " + str(runTot))