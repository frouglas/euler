# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:30:17 2016

@author: frouglas
"""

import math

startVal = math.sqrt(1020304050607080900)

startVal = int(startVal / 10) * 10

found = 0

while found == 0:
    startVal += 10    
    checkVal = startVal ** 2
    checkStr = str(checkVal)
    found = 1    
    for i in range(1,10):
        if checkStr[(i-1)*2] != str(i):
            found = 0            
            break

print str(startVal)
