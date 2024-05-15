def tripletGen(): #generates with Euclid's formula
 for r in range(1,1000):
  for s in range(1,r):
   if ((r**2)/2)%s == 0:
    t = (r**2/2)/s
    if (r+s)+(r+t)+(r+t+s) == 1000: 
     return (r+s)*(r+t)*(r+t+s) #answer = a*b*c
 
 # a = r+s
 # b = r+t
 # c = r+t+s

#Printing the result
print (tripletGen())