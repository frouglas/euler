'''
Created on Aug 25, 2012

A repository for functions that may prove useful later.

@author: frouglas
'''

import math
import random

def parse(x):
    inStr = str(x)
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

def primefactors(x):
    tempfactors = []
    temppower = []
    if x==1:
        factArray = [tempfactors, temppower]
        return factArray
    j = 2
    tempX = x
    while (j <= math.sqrt(x)):
        if prime(j) == 0:
            j += 2
        while tempX % j == 0:
            try: 
                loc = tempfactors.index(j)
                temppower[loc] += 1
            except ValueError:
                tempfactors.append(j)
                temppower.append(1)
            tempX = tempX / j
        if (prime(int(tempX)) == 1) & (tempX!=x):
            tempfactors.append(int(tempX))
            temppower.append(1)
            break
        if j == 2:
            j += 1
        else:
            j += 2
    factArray = [tempfactors, temppower]
    return factArray

def pent(x):
    pentNum = x*(3*x-1)/2
    return pentNum

def isPent(x):
    root = (1+math.sqrt(1+24*x))/6
    if root == int(root):
        return 1
    else: 
        return 0
    
def unparse(arr):
    val = 0
    for i in range(0,len(arr)):
        val += arr[i]*10**(len(arr)-i-1)
    return val

def comb(x,y):
    xFac = math.factorial(x)
    yFac = math.factorial(y)
    diffFac = math.factorial(x-y)
    return xFac/(yFac*diffFac)