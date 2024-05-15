def threeDigitSums():
    product = 0
    sums = []
    for a in range(100,1000):
        for b in range(100,1000): #product of all (100 > x >= 999)
            product = a*b
            if checkPalindrome(product) == ('palindrome'):
              sums.append(product) #only append product == palindrome
    return(sums)

def checkPalindrome(value):
  value = str(value)
  if value == value[::-1]: #if it's the same as itself revered
    return ('palindrome')
  else:
    return ('not palindrome')


pList = (threeDigitSums())
max = 0

for i in range(1,len(pList)):
  if pList[i] > max:
    max = pList[i] #go through pList to find largest palindrome

print(max)
