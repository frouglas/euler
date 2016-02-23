'''
Created on Aug 7, 2012

@author: frouglas

Euler #26: A unit fraction contains 1 in the numerator. The decimal representation of the unit 
fractions with denominators 2 to 10 are given:

1/2    =     0.5
1/3    =     0.(3)
1/4    =     0.25
1/5    =     0.2
1/6    =     0.1(6)
1/7    =     0.(142857)
1/8    =     0.125
1/9    =     0.(1)
1/10    =     0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has 
a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction 
part.

Answer: 983 (repeats 982 times)
'''

uLim = int(input("specify upper bound: "))
uLim += 1
maxRpt = 0
dMax = 0

for i in range(1,uLim):
    remainder=[0 for i in range(0,i)]
    found = 0
    counter = 1
    rem = 1
    while (found == 0):
        rem = rem % i
        if rem == 0:
            break
        elif remainder[rem] == 0:
            remainder[rem] = counter
        else:
            rpt = counter - remainder[rem]
            found = 1
            if rpt>maxRpt:
                maxRpt = rpt
                dMax = i
                print("the longest repeating decimal to this point is 1/" + str(dMax) + " which has a recurring cycle of " + str(maxRpt))
        counter += 1
        rem *= 10

print("the longest repeating reciprocal between 1 and " + str(uLim-1) + " is " + str(dMax) + " which has a recurring cycle of " + str(maxRpt))
