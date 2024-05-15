sumOfSq = 0
sqOfSum = 0
cumulative = 0

for i in range (1,101):
  square = (i**2)
  sumOfSq = sumOfSq + square

for i in range(0,101):
  cumulative = cumulative + i
  print(cumulative)

sqOfSum = cumulative**2

print(sqOfSum - sumOfSq)

#brute force ;)