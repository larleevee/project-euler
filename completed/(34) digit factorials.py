import math

#precalculated to save time
factorials = [math.factorial(0), 
math.factorial(1),
math.factorial(2),
math.factorial(3),
math.factorial(4),
math.factorial(5),
math.factorial(6),
math.factorial(7),
math.factorial(8),
math.factorial(9),]

def factDigSum(factorials, num):
	total = 0
	while num: #goes through all digits
		total += factorials[num%10] #current largest digit
		num //= 10 #sets current to next largest
	return total

runningTotal = 0
for i in range(10,2540161): #upper bound as determind by mathstackexchange (cheers :))
  if factDigSum(factorials, i) == i:
    runningTotal += i

print(runningTotal)