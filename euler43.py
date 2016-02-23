'''
Created on Aug 19, 2012

The number, 1406357289, is a 0 to 9 pandigital number because it is 
made up of each of the digits 0 to 9 in some order, but it also has 
a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, 
    we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

@author: frouglas
'''
import time

startTime = time.clock()

primeList = [1,2,3,5,7,11,13,17]
digits = [0 for j in range(0,10)]
inUse = [0 for j in range(0,10)]
maxCheck = [-1 for j in range(0,10)]
runSum = 0
init = 1
goNext = 0
changed2 = 0
changed3 = 0
changed5 = 0
currNum = ""

for j in range(0,10):
    digits[j] = j
    inUse[j] = 1
    
while maxCheck[0]<9:
    fits = 1
    j = 9
    while j >= 0:
        jVal = j
        maxCheck[j] = digits[j]
        if maxCheck[j]==9:
            j -= 1
            continue
        else:
            inUse = [0 for k in range(0,10)]    
            for k in range(0,jVal):
                if k == 3:
                    while digits[k] % 2 == 1:
                        try:
                            maxCheck[k] = digits[k]
                            newVal = inUse.index(0,digits[k]+1)
                            digits[k] = newVal
                            jVal = k + 1
                            changed2 = 1
                        except ValueError:
                            j = k - 1
                            goNext = 1
                            break
                    inUse[digits[k]] = 1
                elif k == 4:
                    test = sum(digits[l] for l in range(2,5))
                    while sum(digits[l] for l in range(2,5)) % 3 != 0:
                        try:
                            maxCheck[k] = digits[k]
                            newVal = inUse.index(0,digits[k]+1)
                            digits[k] = newVal
                            jVal = k + 1
                            changed3 = 1
                        except ValueError:
                            j = k - 1
                            goNext = 1
                            break
                    inUse[digits[k]] = 1
                elif k == 5:
                    while (digits[k] != 0) & (digits[k] !=5):
                        if digits[k]<5:
                            if inUse[5] == 1:
                                j = k-1
                                goNext = 1
                                break
                            else:
                                digits[k] = 5
                                
                        else:
                            j = k-1
                            goNext = 1
                            break
                    inUse[digits[k]] = 1
                else:
                    inUse[digits[k]] = 1
                currNum += str(digits[k])
                if (changed2==1) | (changed3 == 1) | (changed5 == 1) | (goNext==1):
                    changed2 = 0
                    changed3 = 0
                    changed5 = 0
                    break
            if goNext == 1:
                goNext = 0
                currNum = ""
                continue
            for k in range(jVal,10):
                try:
                    newVal = inUse.index(0,maxCheck[k]+1)
                    if k==3:
                        while newVal % 2 != 0:
                            newVal = inUse.index(0,newVal + 1)
                    elif k==4:
                        sum3 = sum(digits[l] for l in range(2,4)) + newVal
                        while sum3 % 3 != 0:
                            newVal = inUse.index(0,newVal + 1)
                            sum3 = sum(digits[l] for l in range(2,4)) + newVal
                    elif k==5:
                        while (newVal!=5) & (newVal!=0):
                            if newVal<5:
                                if inUse[5] == 1:
                                    j = k
                                    goNext = 1
                                    break
                                else:
                                    newVal = 5
                                    digits[k] = 5
                            else:
                                goNext = 1
                                break
                    if goNext == 1:
                        break
                    digits[k] = newVal
                    inUse[newVal] = 1
                    currNum += str(digits[k])
                    for l in range(k+1,10):
                        maxCheck[l] = -1
                except ValueError:
                    maxCheck[k] = 9
                    goNext = 1
                    break
            if goNext == 1:
                j -= 1
                goNext = 0
                currNum = ""
                continue
            else:
                break
    #print("checking " + currNum + ". . .")
    if maxCheck[0]==9:
        break
    for j in range(1,8):
        if (len(currNum)==0):
            holla = 1
        tempNum = int(currNum[j:j+3])
        rem = tempNum % primeList[j]
        if tempNum % primeList[j] != 0:
            #print("    " + currNum[j:j+3] + " / " + str(int(primeList[j])) + " != " + str(int(currNum[j:j+3])/primeList[j]))
            fits = 0
            break
        else:
            holla = 1
            #print("    " + currNum[j:j+3] + " / " + str(int(primeList[j])) + " = " + str(int(currNum[j:j+3])/primeList[j]))
    if fits:
        runSum += int(currNum)
        print(currNum  + " has the special property, running sum = " + str(runSum))
    currNum = ""
print("the sum of the select numbers in " + str(runSum))
endTime = time.clock()
elapsed = endTime - startTime
elaMin = int(elapsed / 60)
elaSec = elapsed-60*elaMin
print("time elapsed: " + str(elaMin) + " minutes, " + str(elaSec) + " seconds ")
            
        
        