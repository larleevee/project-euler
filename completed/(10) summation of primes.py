sieve = [True] * 2000000 #initialise sieve of erathththth
sieve[0] = False #not prime
sieve[1] = False #not prime


for multiplier in range(2, 2000000):
    i = multiplier * 2
    while i < 2000000:
        sieve[i] = False #index of prime == false
        i += multiplier #goes to next value which matters (if //6 then can //3...)


total = 0
for j in range(2000000):
    if sieve[j]:
        total += j #sum all elements

print(total)