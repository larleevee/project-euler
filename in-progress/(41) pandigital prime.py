def isPandigital(n):
    number = str(n)
    digits = []
    for digit in number:
        if digit in digits:
            return False
        else:
            digits.append(digit)
    goal = []
    for x in range(1, len(number)+1):
        goal.append(str(x))

    if goal == sorted(digits):
        return True
    else:
        return False

def isPrime(num):
    if (num == 2) or (num == 3): #special case
        return True
    if (num % 2 == 0) or (num < 2): #special case & all even
        return False
    for n in range(3 ,int(num**0.5)+1, 2):  #every 2 (all odds) up to sqrt  
        if (num % n == 0):
            return False   
    return True # must be prime

panPrimes = []

for i in range(1,987654321+1,2):
  if isPandigital(i) == True:
    if isPrime(i) == True:
      panPrimes.append(i)

print(panPrimes[-1])
    