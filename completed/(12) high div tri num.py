import math

def getFactors(number):
    factorList = [] #all factors are below sqrt because math i guess? 
    for factor in range(1, int(math.sqrt(number)) + 1): 
        if number % factor == 0:
            factorList.append(factor) #append factor
            factorList.append(number // factor) #append factor
    return int(len(factorList)) #returns amount of factors

def triangleGen(n):
    xthNum = int(0)
    xthNum = (n*(n+1)/2) #formula for triangle num
    return xthNum

factorCount = 0
triIndex = 1

while factorCount <= 500:
  triangle = (triangleGen(triIndex))
  factorCount = (getFactors(triangle))
  print(triIndex, triangle, factorCount)
  triIndex +=1

print(triangle)