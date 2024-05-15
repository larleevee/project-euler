# primes before number =~ number / log(number)

import math

def nthPrime(n): #n = position of prime we're looking for
  listLen = 100
  while listLen / math.log(listLen) < n * 3: #large margin of error (*3 the estimate)
    listLen *= 2 #if est too low, double length and try again

  isPrimeList = [True]*listLen
  primeCount = 0
  for i in range(2, listLen):
    if isPrimeList[i]:
      k = i*i
      while k < listLen:
        isPrimeList[k] = False #turns all primes FALSE
        k += i
      primeCount += 1
      if primeCount == n:
        return(isPrimeList[:i+1])

print(len(nthPrime(10001))-1)