def sieve(n): #n=max

	isPrime = [True]*n
	isPrime[0] = False
	isPrime[1] = False

	for i in range(2,int(n**0.5+1)): #all factors under sqrt

		index = i*2

		while index < n:
			isPrime[index] = False #all multiples aren't prime
			index = index+i

	prime = [] #list of all primes under n

	for i in range(n):
		if isPrime[i] == True:
			prime.append(i)

	return prime

def isPrime(num):
    if (num == 2) or (num == 3): #special case
        return True
    if (num % 2 == 0) or (num < 2): #special case & all even
        return False
    for n in range(3 ,int(num**0.5)+1, 2):  #every 2 (all odds) up to sqrt  
        if (num % n == 0):
            return False   
    return True # must be prime

primes1000 = sieve(1000)
primes = primes1000[:] #copy of primes1000
largest = 0


# n^2 + an + b

for b in primes1000: #iterates through all quads
  for a in primes1000: 
    i = 0
    while True:  # +a +b
      quadratic = i**2+a*i+b

      if quadratic not in primes:
        if isPrime(quadratic):
          primes.append(quadratic)
        else:
          if i-1 > largest:
            largest = i-1
            axb = a*b #product for solution
          break
      i += 1
    i = 0
    while True: # -a +b
      quadratic = i**2-a*i+b
      if quadratic not in primes:
        if isPrime(quadratic) and quadratic > 0:
          primes.append(quadratic)
        else:
          if i-1 > largest:
            largest = i-1
            axb = -1*a*b #abs val
          break
      i += 1

print(axb)