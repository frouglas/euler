'''
Created on May 19, 2011

@author: frouglas
'''

import math

def isPal(num):
    pal = 1
    num = str(num)
    for i in range(0,math.floor(len(num)/2)):
        if num[i] == num[-(i+1)]:
            continue
        else:
            pal = 0
            break
    return pal

def convBin(num):
    bin = ""
    i = 0
    while math.pow(2,i+1) <= num:
        i += 1
    for j in range(i,-1,-1):
        dig = "0"
        while math.pow(2,j) <= num:
            num -= math.pow(2,j)
            dig = "1"
        bin = bin + dig
        if num == 0:
            for k in range(j,0,-1):
                bin += "0"
            break
    return bin

sum = 0

for i in range(1,1000001):
    if isPal(i):
        bin = convBin(i)
        if isPal(bin):
            sum += i
            print(str(i) + ", " + bin + ", running count = " + str(sum))
print("there are " + str(sum) + " numbers that are palindromes in both base 10 and base 2 between 1 and 1,000,000")