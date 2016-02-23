'''
Created on May 18, 2011

Surprisingly there are only three numbers that can be written as the 
sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.

ANSWER: 443839

@author: frouglas
'''

import math

dig = []
dig.append(2)
total = 0

while math.pow(10,len(dig)-1) < math.pow(9,5) * len(dig):
    sum = 0
    digStr = ""
    allUsed = 1
    for i in dig:
        sum += int(math.pow(i,5))
    checkSum = str(sum)
    for i in dig:
        if checkSum.find(str(i)) == -1:
            allUsed = 0
            break
        else:
            checkSum = checkSum.replace(str(i), "-",1)
            digStr += str(i)
    if allUsed:
        for i in checkSum:
            if i =="0" or i =="-":
                continue
            else:
                allUsed = 0
                break
        if allUsed:
            total += sum
            print(digStr + ", " + str(sum) + ", running total " + str(total))
    for i in range(-1, -len(dig)-1, -1):
        if dig[i] == 9:
            if -i == len(dig):
                for i in range(0,len(dig)):
                    dig[i] = 1
                dig.append(1)
            else:
                continue
        else:
            newVal = dig[i] + 1
            for j in range(len(dig) + i, len(dig)):
                dig[j] = newVal
            break
            
                
        
            
        