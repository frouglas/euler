'''
Created on May 17, 2011

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many 
letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing 
out numbers is in compliance with British usage.

ANSWER: 21124

@author: frouglas
'''
def digits(n):
    isTeen = 0
    teenAdder = 0
    oneAdder = 0
    tenAdder = 0
    hunAdder = 10
    thouAdder = 8
    n = str(n)
    dig = []
    for i in range(0,4):
        if i < len(n):
            dig.append(int(n[-i-1]))
        else:
            dig.append(0)
    if dig[1] == 1:
        isTeen = 1
        teen = int(str(dig[1])+str(dig[0]))
        if teen == 10:
            teenAdder = 3
        elif teen == 11 or teen == 12:
            teenAdder = 6
        elif teen == 13 or teen == 14 or teen == 18:
            teenAdder = 8
        elif teen == 15:
            teenAdder = 7
        else:
            isTeen = 0
    if isTeen == 0:       
        if dig[0] == 0:
            oneAdder = 0
        elif dig[0] == 1 or dig[0] == 2 or dig[0] == 6:
            oneAdder = 3
        elif dig[0] == 3 or dig[0] == 7 or dig[0] == 8:
            oneAdder = 5
        else:
            oneAdder = 4
        if dig[1] == 0:
            tenAdder = 0
            if dig[0] == 0:
                hunAdder -= 3
        elif dig[1] == 1:
            tenAdder = 4
        elif dig[1] == 4 or dig[1] == 5 or dig[1] == 6:
            tenAdder = 5
        elif dig[1] == 7:
            tenAdder = 7
        else:
            tenAdder = 6
    if dig[2] > 0:
        if dig[2] == 1 or dig[2] == 2 or dig[2] == 6:
            hunAdder += 3
        elif dig[2] == 3 or dig[2] == 7 or dig[2] == 8:
            hunAdder += 5
        else:
            hunAdder += 4
    else:
        hunAdder = 0
    if dig[3] > 0:
        if dig[3] == 1 or dig[3] == 2 or dig[3] == 6:
            thouAdder += 3
        elif dig[3] == 3 or dig[3] == 7 or dig[3] == 8:
            thouAdder += 5
        else:
            thouAdder += 4
    else:
        thouAdder = 0
    total = teenAdder + oneAdder + tenAdder + hunAdder + thouAdder
    return total


count = int(0)

uBound = int(input('specify upper bound for summation: '))
breakPt = int(input('specify break point for debugging: '))

for i in range(0,uBound):
    if i > 0 and i == breakPt:
        breakPt = 0
    adder = digits(i+1)
    print("digits in " + str(i+1) + " : " + str(adder))
    count += adder
    
print("there are "+ str(count) + " digits in the names of numbers up to " + str(uBound))
    


    