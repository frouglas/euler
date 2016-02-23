'''
Created on May 17, 2011

@author: frouglas
'''

uBound = int(input('specify an upper bound: '))
total = 0

for i in range(1, uBound + 1):
    adder = str(pow(i,i))
    if len(adder) > 10:
        startPos = len(adder)-10
        endPos = len(adder)
        adder = adder[startPos:endPos]
    total += int(adder)
    if len(str(total)) > 10:
        startPos = len(str(total))-10
        endPos = len(str(total))
        total = int(str(total)[startPos:endPos])
    print("last ten digits of " + str(i) + "^" + str(i) + " are " + adder + ", running total: " + str(total))