source("eulerFuncs.R")

uLim <- getLim()

thisFib <- rep(1, times=2)
runTotal <- 0
while (thisFib[2]<=uLim) {
  fibAdd <- thisFib[as.integer(thisFib/2)==thisFib/2]
  runTotal <- runTotal + sum(fibAdd)
  thisFib <- nextFib(thisFib[1], thisFib[2])
}
if (thisFib[1]<=uLim && (as.integer(thisFib[1]/2)==thisFib[1]/2)) {
  runTotal <- runTotal + thisFib[1]
}
print(cat("the total sum of fibonacci numbers less than ",as.character(uLim) ," is: ",as.character(runTotal)))