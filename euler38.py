'''
Created on Aug 17, 2012

@author: frouglas


Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 

We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?

'''

def parse(inStr):
    inStr = str(inStr)
    temp = []
    for i in range(0,len(inStr)):
        temp.append(int(inStr[i]))
    return temp

tooShort = 1
i = 1
j = 1
maxPandi = 0

while tooShort==1:
    j=1
    digits = []
    numCon= 0
    holder = 0
    present = [0 for i in range(0,9)]
    pandi = 1
    while len(str(numCon))<9:
        holder = i * j
        numCon = numCon*10**len(str(holder)) + holder
        j += 1
    digits = parse(numCon)
    if len(digits)==9:
        for k in digits:
            if present[k-1]==0:
                present[k-1]=1
            else:
                pandi = 0
                break
        for k in present:
            if k==0:
                pandi = 0
                break
        if pandi == 1:
            print("concatenating products of " + str(i) + " produces a pandigital number, " + str(numCon))
            maxPandi = max(maxPandi,numCon)
    i+=1
    if ((len(digits)>9) & (j==3)):
        tooShort = 0
print("the largest pandigital number that can be produced by concatenation is " + str(maxPandi))
        
        