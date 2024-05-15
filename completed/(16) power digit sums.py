startNum = 2**1000
digitList = []
numHolder = 0
total = 0

for a in str(startNum):
  digitList.append(a)

print(digitList)
print(len(digitList))

for i in range (0,(len(digitList))):
  numHolder = int(digitList[i])
  total = total + numHolder

print(total)

#literally just brute force lol