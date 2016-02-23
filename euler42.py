'''
Created on Aug 19, 2012

 the first 
ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value. For example, the word value for 
SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle words?

ANSWER: 162

@author: frouglas
'''

import math

input=[]
lastWord = 0
triCont = 0

f = open('/Users/frouglas/Documents/projecteuler/words.txt','r')
for line in f:
    line = line.rstrip()

while lastWord==0:
    wordVal = 0
    startPos = int(line.index('''"''')+1)
    endPos = int(line.index('''"''',startPos+1))
    currWord = line[startPos:endPos]
    if endPos == len(line)-1:
        lastWord = 0
    else:
        line = line[endPos+2:]
    for i in range(0,len(currWord)):
        letterVal = ord(currWord[i])-64
        wordVal += letterVal
    triNum = -0.5 + math.sqrt(0.25+2*wordVal) 
    if int(triNum) == triNum:
        triCont += 1
        print(currWord + " is a triangle word, value = " + str(wordVal) + ", triangle base = " + str(int(triNum)) + ", total found: " + str(triCont))
        
    
