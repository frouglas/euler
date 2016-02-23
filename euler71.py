# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:50:00 2016

@author: frouglas
"""

from pyFuncs import primefactors 
import math

runList = []
ceiling = float(3)/7
maxFound = 0
commonFac = 0
maxI = 0
maxN = 0
n = 1000000
 
while n > 2:
    if int(n/10000) == float(n)/10000:
        print("checking n = " + str(n) + "...")
    i = math.ceil(n * ceiling)
    i = int(i)
    n = int(n)
    if ((n%2) == 0) & ((i&2)==0):
        i -= 1
    prop = float(i)/n
    while prop > maxFound:
        if prop < ceiling:
            numFacs = primefactors(i)
            if numFacs != [[],[]]:            
                denFacs = primefactors(n)
                if (denFacs != [[],[]]):
                    for j in numFacs[0]:
                        if denFacs[0].count(j) != 0:
                            commonFac = 1                
                            break
            if commonFac == 1:
                commonFac = 0
            else:
                maxFound = prop
                maxI = i
                maxN = n
        i -= 2 - (n%2)
        prop = float(i) / n
    n -= 1

print str(maxI) + "/" + str(maxN) + " = " + str(maxFound)
