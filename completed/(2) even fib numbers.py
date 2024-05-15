fib = [1, 2] #start of fib chain
total = 0

while fib[-1] <= 4000000: #while largest value below ceiling
  newFib = fib[-1] + fib[-2] #make new digit
  fib.append(newFib)

fib.pop(-1) #last fib is above anyway thanks while loop
print(len(fib))

for i in range (0,32):
  if fib[i] % 2 == 0: #even terms
    total = total + fib[i] #sum

print(total)