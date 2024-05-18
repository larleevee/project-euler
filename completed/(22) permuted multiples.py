def intoDigits(number): #seperates int into list of int(digits)
  digits = []
  while number >= 1:
    nextDigit = number % 10
    digits.append(nextDigit)
    number = number // 10
  return digits

def isPerm(xval, mult):
  
  num1 = intoDigits(xval)
  num2 = intoDigits(mult)
  
  num1.sort()
  num2.sort()

  if num1 == num2:
    return True

  return False

x = 100000
found = False
while found == False:
  x2 = x*2
  if isPerm(x, x2):
    x3 = x*3
    if isPerm(x,x3):
      x4 = x*4
      if isPerm(x,x4):
        x5 = x*5
        if isPerm(x,x5):
          x6 = x*6
          if isPerm(x,x6):
            found = True
            print('x = {} \n2x = {} \n3x = {} \n4x = {} \n5x = {} \n6x = {}'.format(x,x2,x3,x4,x5,x6))
  x += 1

  