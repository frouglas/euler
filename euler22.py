'''
Created on May 18, 2011

Using names.txt (right click and 'Save Link/Target As...'), a 46K text 
file containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would 
obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?

ANSWER: 871198282

@author: frouglas
'''
import math

def nameVal(name):
    sum = 0
    for i in range(0,len(name)):
        sum += ord(name[i]) - 64
    return sum

names = []
sortNames = []
total = 0
f = open('/Users/frouglas/Documents/names.txt','r')
allNames = f.readline()
names = allNames.split(',')
for i in range(0,len(names)):
    names[i] = names[i].strip('\"')
    if i == 0:
        sortNames.append(names[i])
    else:
        j = 0
        while names[i] > sortNames[j]:
            j += 1
            if j == len(sortNames):
                break
        sortNames.insert(j,names[i])
for i in range(0,len(sortNames)):
    total += nameVal(sortNames[i]) * (i+1)
    print("Position " + str(i+1) + ", " + sortNames[i] + ", Name Value = " + str(nameVal(sortNames[i])) + ", Running Total = " + str(total))



    
    
    