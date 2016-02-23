'''
Created on Aug 14, 2012

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and 
product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through
9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


@author: frouglas
'''

def reset(inArray,startPos = 0,endPos = -1, resetval = 0):
    if endPos == -1:
        endPos = len(inArray)
    for i in range(startPos,endPos):
        inArray[i] = resetval
    return inArray
        

inUse = [0 for i in range(0,9)]
currProg = [-1 for i in range(0,9)]
currDig = [0 for i in range(0,9)]
failed = -1
foundPairs = []
runSum = 0

for i in range(1,5):
    print("i = " + str(i))
    for j in range(i,9-i):
        print("    j = " + str(j))
        minI = 10**(i-1)
        maxI = 10**(i)-1
        minJ = 10**(j-1)
        maxJ = 10**(j)-1
        minProd = 10**(9-i-j-1)
        maxProd = 10**(9-i-j)-1
        if (minI * minJ > maxProd) | (maxI * maxJ < minProd):
            continue
        currProg = reset(currProg, resetval=-1)
        currDig = reset(currDig)
        currDig[0] = 1
        currProg[0] = 0
        while currDig[0]<10:
            inUse = reset(inUse)
            inUse[currDig[0]-1] = 1
            iNum = currDig[0]*(10**(i-1))
            jNum = 0
            for k in range(1,i+j):
                try:
                    dig = inUse.index(0,max(currProg[k],0)) + 1
                except ValueError:
                    failed = k
                    break
                inUse[dig-1] = 1
                if currProg[k]==-1:
                    currProg[k] = dig - 1
                if k<i:
                    currDig[k] = dig
                    iNum += dig*(10**(i-k-1))
                else:
                    currDig[k] = dig
                    jNum += dig*(10**(j-k+i-1))
            if failed != -1:
                for k in range(failed,0,-1):
                    if k==1:
                        currDig[k-1] += 1
                        failed = -1
                        currProg = reset(currProg,k,i+j)
                        break
                    else:
                        if currDig[k-1]==9:
                            continue
                        else:
                            currProg[k-1] += 1              
                            currProg = reset(currProg,k,i+j)
                            failed = -1
                            break
                continue
            #print("testing " + str(iNum) + " * " + str(jNum))           
            numProd = round(iNum * jNum,0)
            prodLen = len(str(numProd))
            if i + j + prodLen == 9:
                found = 1
                for k in range(0,prodLen):
                    dig = int(str(numProd)[k])
                    if (inUse[dig-1] == 1):
                        found = 0
                        break
                    elif dig==0:
                        found = 0
                        break
                    else:
                        inUse[dig-1] = 1
                if found == 1:
                    try:
                        present = foundPairs.index(numProd)
                        print("**      " + str(iNum) + " * " + str(jNum) + " = " + str(numProd))
                    except ValueError:
                        foundPairs.append(numProd)
                        runSum += numProd
                        print("        " + str(iNum) + " * " + str(jNum) + " = " + str(numProd))
            for k in range(i+j,0,-1):
                if currDig[k-1]==9:
                    continue
                if k < i + j:
                    currProg = reset(currProg,k,i+j)
                if k==1:
                    currDig[k-1] += 1
                else:
                    currProg[k-1] = currDig[k-1]
                break
print("the sum of the products is " + str(runSum))
            
                    
                
                    
            
                
                
                 
            
               
            