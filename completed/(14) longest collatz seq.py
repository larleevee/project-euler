def nextLink(num): #get next value and smack it on chain
    chain = [num]
          
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
            chain.append(num)
        elif num % 2 == 1:
            num = (num * 3) + 1
            chain.append(num)
          
    return chain
         

chainLen = 0
largestNum = 0
         
for i in range(1, 1000000):
    if i % 2 != 0:
        if len(nextLink(i)) > chainLen:
            largest = len(nextLink(i))
            largestNum = i
              
print('LARGEST INPUT')
print(largestNum)
print('CHAIN LENGTH')
print(chainLen)
