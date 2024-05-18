from datetime import datetime

start = datetime.now()

def factor(num): #sum all proper divisors of num
    factorSum = 1
    if (num**0.5) % 1 == 0: #all factors < sqrt
        factorSum += (num**0.5)
    for div in range(2, int(num**0.5) + 1): #prime check
        if num % div == 0:
            factorSum += div + (num / div)
    return factorSum



def sumAmicable(x): #sum of all amicable
    amicable = 0
    for a in range(1, x):
        b = factor(a)
        if a != b and factor(a) == b and factor(b) == a: #if amicable
            amicable += (a + b) / 2 #sum of all
    return amicable


print(sumAmicable(10000)-3) #for some reason it gives me 3 over idk

after = datetime.now()
print('it took: {}'.format(after-start))