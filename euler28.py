'''
Created on May 18, 2011

Starting with the number 1 and moving to the right in a clockwise direction a 
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

ANSWER: 669171001

@author: frouglas
'''

sideLength = 3
total = 1
counted = 0
runCount = 1

uBound = int(input('Specify the size of the spiral for which diagonals will be counted: '))

while sideLength <= uBound:
    runCount += sideLength - 1
    total += runCount
    counted += 1
    if counted == 4:
        sideLength += 2
        counted = 0
print("the sum of the diagonals in a " + str(uBound) + " x " + str(uBound) + " spiral is " + str(total))
    
    