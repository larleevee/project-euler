def intoDigits(number): #seperates int into list of int(digits)
  digits = []
  while number >= 1:
    nextDigit = number % 10
    digits.append(nextDigit)
    number = number // 10
  return digits

def fifthPowerSum(number):
  digits = intoDigits(number)
  powerSum = 0
  for i in range (0, len(digits)):
    powerSum += (digits[i])**5
  return powerSum

runningSum = 0
for i in range(2, 355000):
  if i == fifthPowerSum(i):
    runningSum += i

print(runningSum)