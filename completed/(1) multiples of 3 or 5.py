multiples = []
finalScore = 0
mult1 = False
mult2 = False

for i in range (1,1000):
  if (i % 3) == 0:
    mult1 = True
  elif (i % 5) == 0:
    mult2 = True

  if mult1 or mult2 == True:
    multiples.append(i)
    finalScore = finalScore + i
  
  mult1 = False
  mult2 = False

print(multiples)
print(finalScore)