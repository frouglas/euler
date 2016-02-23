'''
Created on Aug 18, 2012

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000

ANSWER: 210

@author: frouglas
'''

fracStr = ""
i = 1

while len(fracStr) < 1000000:
    fracStr = fracStr + str(i)
    i += 1

d1 = int(fracStr[0])
d11 = int(fracStr[9])
d12 = int(fracStr[99])
d13 = int(fracStr[999])
d14 = int(fracStr[9999])
d15 = int(fracStr[99999])
d16 = int(fracStr[999999])

finProd = d1*d11*d12*d13*d14*d15*d16

print("the product is " + str(finProd))
