source("eulerFuncs.R")

factors <- primeFac(600851475143)
maxFact <- max(factors)

print("the max prime factor is: ")
print(as.character(maxFact))