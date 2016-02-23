'''
Created on May 18, 2011

Let d(n) be defined as the sum of proper divisors of n (numbers less 
than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 
4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

ANSWER: 31626

@author: frouglas
'''

import math

factors = [[1] for i in range(0,10000)]
factorSums = [[] for i in range(0,10000)]
amicableSum = 0

for i in range(2,10001):
    sum = 0
    j = 2
    while j <= math.sqrt(i):
        if i % j == 0:
            factors[i-1].append(j)
            if j != 1 and i / j != j:
                factors[i-1].append(int(i/j))
        j += 1
    for j in factors[i-1]:
        sum += j
    if sum < i:
        if factorSums[sum - 1] == i:
            amicableSum += i
            amicableSum += sum
            print(str(i) + ", " + str(sum) + ", running total of amicable numbers = " + str(amicableSum))
    else:
        factorSums[i-1] = sum
        
             
        