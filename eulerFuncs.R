nextFib <- function(fib1, fib2) {
  nextF <- rep(0, times=2)
  nextF[1] <- fib1 + fib2
  nextF[2] <- nextF[1] + fib2
  return(nextF)
}

getLim <- function() {
  lim <- readline("input upper limit: ")
  return(as.integer(lim))
  print("test")
}

primeList <- function(lim, primes) {
  if (length(primes)==0) {
    init = 2
  } else {
    init = max(primes) + 1
  }
  pri = 1
  for (i in primes) {
    if (i > sqrt(init)) break
    if (init %% i == 0) {
      pri = 0
      break
    }     
  }
}

nextPrime <- function(primes) {
  if (length(primes)==0) {
    init = 1
  } else {
    init = max(primes)
  }
  notFound <- TRUE
  while (notFound) {
    notFound <- FALSE
    init <- init + 1
    for (i in primes) {
      if (i > sqrt(init)) break
      if (init %% i == 0) {
        notFound <- TRUE
        break
      }
    }
  }
  return(init)
}

primeFac <- function(fact, breakout = FALSE, suppress = FALSE) {
  factors <- vector()
  origFact <- fact
  if (length(primes)==0) primes <<- append(primes,nextPrime(primes))
  maxP <- max(primes)
  while (maxP<=sqrt(fact)) {
    maxP <- nextPrime(primes)
    primes <<- append(primes, maxP)
  }
  assign("primes", primes, envir = .GlobalEnv)
  for (i in primes) {
    if (i > sqrt(origFact)) break
    while (fact %% i == 0) {
      if (breakout) {
        return(FALSE)
      }
      fact <- fact / i
      factors <- append(factors, i)
    }
  }
  if (fact == 1) {
    if (breakout) return(FALSE)
    return(factors)
  }
  if (breakout) return(TRUE)
  factors <- append(factors, fact) 
  return (factors)
}