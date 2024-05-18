def divisors(n):
	divs = [1]
	for i in range(2,int(n**0.5)+1):
		if n%i == 0:
			divs.extend([i,n/i]) #seamless join 2 lists
	return list(set(divs)) #no duplicates

abunds = []

for i in range(12,28123):
	if sum(divisors(i))>i:
		abunds.append(i)

nonAbunds = [x for x in range(28123)] #assuming all aren't abund

for i in range(len(abunds)):
	for j in range(i,28123):
		if abunds[i]+abunds[j] < 28123:
			nonAbunds[abunds[i]+abunds[j]] = 0 #removing all abund
		else:
			break

print (sum(nonAbunds))