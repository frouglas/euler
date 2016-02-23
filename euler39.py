'''
Created on Aug 18, 2012

If p is the perimeter of a right angle triangle with integral 
length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?

ANSWER = 840

@author: frouglas
'''

import math

maxICount = 0
maxI = 0
combos = [0 for i in range(0,1000)]

for i in range(1,501):
    if int(i/50) == i/50:
        print("i = " + str(i))
    for j in range(0,i+1):
        i2 = (i+1)**2
        j2 = (j+1)**2
        z = math.sqrt(i2+j2)
        if i + j + z + 2 > 1000:
            break
        if int(z) == z:
            combos[int(i+j+z+2)-1] += 1
            print("    " + str(i+1) + ", " + str(j+1) + ", " + str(int(z)) + ", total perimeter = " + str(int(i+j+z+2)))
maxICount = max(combos)
maxI = combos.index(maxICount, ) + 1
print("the most combinations is " + str(maxICount) + ", i = " + str(maxI))

                
            