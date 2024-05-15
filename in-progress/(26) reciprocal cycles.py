def recurringDecimal(divisor): #basically just long division, I hate long division

  if divisor <10:
    divident = 10
  elif divisor >=10 and divisor <100:
    divident = 100
  else: 
    divident = 1000

  checkVal = divident #10 or 100 or 1000
  string = ''

  for i in range(divisor):
    string += str(divident/divisor)
    divident = divident % divisor

    if divident < divisor:#adding decimal
      divident *= 10

      if divident < divisor:#adding zero after decimal
        divident *= 10
        string += '0'

        if divident < divisor:#adding another decimal after 0
          divident *= 10
          string += '0'

    if divident == checkVal:
      return string

def sieve(n): #eratosthenes

	isPrime = [True]*n
	isPrime[0] = False
	isPrime[1] = False

	for i in range(2,int(n**0.5+1)):

		index = i*2

		while index < n:
			isPrime[index] = False
			index = index+i

	prime = []

	for i in range(n):
		if isPrime[i] == True:
			prime.append(i)

	return prime

def gcd(n1,n2): #euclidean algorithm
  while n2 != 0:
    temp = n2
    n2 = n1 % n2
    n1 = temp
    return n1

def lcm(n1,n2): #wikimath said so idk??
  return (n1*n2)/gcd(n1,n2)

#idk where to go from here lol
