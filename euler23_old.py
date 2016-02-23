'''
Created on May 27, 2011

@author: frouglas
'''
import random

def parsestring(x):
        tempstring = x
        seqsum = ''
        ttt = 0
        while ((len(tempstring)>0) & (tempstring.find('sc') > -1) & (ttt < 100)):
                index = tempstring.find('sc')
                seqsum = seqsum + str(index)
                tempstring = tempstring[index+2:]
                ttt = ttt + 1
        seqsum = seqsum + str(len(tempstring))
        return seqsum

n = 200
howmany = [0]
sequence = ['']
seqsum = ['']

for i in range(1,n+1):
        if(i<7):
                howmany.append(i)
                sequence.append(sequence[i-1]+'p')
        else:
                howmanynew=1
                for j in range(2,int(i/2+1)):
                        temp = howmany[j]*howmany[i-j-1]
                        if temp > howmanynew:
                                howmanynew=temp
                                numgroups = j
                                groupsize = i-j-1
                howmany.append(howmanynew)
                sequence.append(sequence[groupsize]+'sc'+sequence[numgroups][1:])
        seqsum.append(parsestring(sequence[i]))
        print(i,str(howmany[i]),seqsum[i])
                