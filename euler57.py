'''
Created on Sep 1, 2012

@author: frouglas
'''

iter = 1
numN = 3
numN1 = 1
numHolder = 0
denomN = 2
denomN1 = 1
denomHolder = 0
found = 0

for i in range(0,1000):
    estim = numN / denomN
    if len(str(numN)) > len(str(denomN)):
        found += 1
        print("the " + str(iter) + "th expansion:" + str(numN) + " / " + str(denomN) + ", total found = " + str(found))
    numHolder = numN
    denomHolder = denomN
    numN = 2*numN + numN1
    numN1 = numHolder
    denomN = 2*denomN + denomN1
    denomN1 = denomHolder
    iter += 1
    
    