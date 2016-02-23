'''
Created on Aug 15, 2012

The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which 
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find 
the value of the denominator.

@author: frouglas
'''

advanceI = 0
advanceJ = 0
advanceK = 0

numers = []
simpNumers = []
denoms = []
simpDenoms = []

for i in range(1,10):
    for j in range(i,10):
        for k in range(1,10):                      
            for iPos in range(0,2):
                for denomVar in range(0,2):
                    for kPos in range(0,2):
                        numer = (i*10**(1-iPos))+(j*10**(iPos))
                        denom = (k*10**(1-kPos))+(((1-denomVar)*i+denomVar*j)*10**(kPos))
                        if numer>=denom:
                            break
                        ratio = numer / denom
                        if (ratio == (denomVar*i+(1-denomVar)*j)/(k)):
                            try: 
                                denoms.index(denom)
                                try:
                                    numers.index(numer)
                                    break
                                except ValueError:
                                    denoms.append(denom)
                                    numers.append(numer)
                                    simpDenoms.append(k)
                                    simpNumers.append(denomVar*i+(1-denomVar)*j)
                                    print(str(numer) + "/" + str(denom) + " = " + str(denomVar*i+(1-denomVar)*j) + "/" + str(k))               
                            except ValueError:
                                denoms.append(denom)
                                numers.append(numer)
                                simpDenoms.append(k)
                                simpNumers.append(denomVar*i+(1-denomVar)*j)
                                print(str(numer) + "/" + str(denom) + " = " + str(denomVar*i+(1-denomVar)*j) + "/" + str(k))
                        if (denomVar==0 & i==k) | (denomVar==1 & k==j):
                            break
                if (i==j):
                    break

prodNumers = 1
prodDenoms = 1

for i in range(0,len(numers)):
    prodNumers *= simpNumers[i]
    prodDenoms *= simpDenoms[i]

prodDenoms = prodDenoms / prodNumers
print("the value of the denominator is " + str(int(prodDenoms)))
    