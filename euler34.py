'''
Created on May 18, 2011

@author: frouglas
'''

import math

dig = []
dig.append(3)
total = 0

while math.pow(10,len(dig)-1) < math.factorial(9) * len(dig):
    sum = 0
    digStr = ""
    allUsed = 1
    for i in dig:
        sum += int(math.factorial(i))
        digStr += str(i)
    if sum == int(digStr):
        total += sum
        print(digStr + ", " + str(sum) + ", running total " + str(total))
    for i in range(-1, -len(dig)-1, -1):
        if sum > int(digStr):
            if dig[i] == 0:
                continue
            dig[i] = 0
            if i - 1 < -len(dig):
                dig.insert(0,1)
            else:
                if dig[i-1] == 9:
                    dig[i-1] = 0
                    dig.insert(0,1)
                else:
                    dig[i-1] += 1
                break
        else:
            if dig[i] == 9:
                dig[i] = 0
                if i - 1 == -len(dig):
                    dig.insert(0,1)
                else:
                    dig[i-1] += 1
            else:
                dig[i] += 1
                break
print("The total is " + str(total))