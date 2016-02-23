'''
Created on Sep 1, 2012

@author: frouglas
'''

import copy

from pyFuncs import parse, unparse

lychs = 0

for i in range(1,10001):
    lychrel = 1
    activeNum = 0
    if int(i/1000)==i/1000:
        print("checking " + str(i) + " . . .")
    activeNum = i
    rep = 0
    digits = parse(activeNum)
    while (lychrel == 1) & (rep<=50):
        revDigits = copy.copy(digits)
        revDigits.reverse()
        adder = unparse(revDigits)
        activeNum += adder
        digits = parse(activeNum)
        rep += 1
        for j in range(0,int(len(digits)/2)+1):
            if digits[j] != digits[len(digits) - j -1]:
                break
            elif j == int(len(digits)/2):
                lychrel = 0
    if lychrel == 1:
        lychs += 1
        print(str(i) + " is a lychrel number, " + str(lychs) + " lychral numbers found")
            