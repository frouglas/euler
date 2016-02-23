# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:02:54 2016

@author: frouglas
"""

def nSums(n):
    if n == 2:
        return 1
    else:
        return nSums(n-1) + int(n/2)
        
baseNum = input("what number would you like to decompose? ")
result = nSums(baseNum)

print "     " + str(baseNum) + " can be expressed in " + str(result) + " ways as the sum of two positive integers"