import math

total = 0
valList = []
fact = str((math.factorial(100))) #int -> str so digits can be removed with len()

for i in range(len(fact)):
  valList.append(fact[i]) #takes single digit from 100!
  valList[i] = int(valList[i])
  total += valList[i] #sums all list elements

print(total)