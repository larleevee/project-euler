import math

def getFactors(number):
    factors = [] #all factors are below sqrt because math i guess? 
    for potentialPrimeFactor in range(1, int(math.sqrt(number)) + 1): 
        if number % potentialPrimeFactor == 0:
            factors.append(potentialPrimeFactor) #append factor
            factors.append(number // potentialPrimeFactor) #append factor
    return factors #all factors of number

def isPrime(number):
    return len(getFactors(number)) == 2  #JUST TRUST ME IT WORKS (?)

allFactors = getFactors(600851475143)

largestPrimeFactor = 0
for factor in allFactors:
    if isPrime(factor) and factor > largestPrimeFactor:
        largestPrimeFactor = factor #goes through all prime factors to find the largest

print(largestPrimeFactor)