def nextFib(fibList):
  newFib = fibList[-1] + fibList[-2] #make new digit
  fibList.append(newFib)
  return fibList

fibList = [1,1]
lastFib = fibList[-1]

while len(str(lastFib)) != 1000:
  fibList = nextFib(fibList)
  lastFib = fibList[-1]


print(len(fibList))
