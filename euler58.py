'''
Created on Sep 1, 2012



@author: frouglas
'''

import copy
from pyFuncs import prime

checked = 1
found = 0
spiRatio = 1
i = 1
activeNum = 1
j = 0
    
while (spiRatio > 0.1):
    if (int((i-1)/100)==((i-1)/100)) & (i>1):
        spiStr = str(round(spiRatio,6))
        print("the " + str(i) + "th grid (" + str(j + 1) + "x" + str(j + 1) + ") has a diagonal ratio of " + spiStr)
    j = 2*i
    for k in range(0,4):
        activeNum += j
        checked += 1
        if prime(activeNum)==1:
            found += 1
    spiRatio = found / checked
    i += 1
spiStr = str(round(spiRatio,6))
print("the " + str(i) + "th grid (" + str(j + 1) + "x" + str(j + 1) + ") has a diagonal ratio of " + spiStr)
