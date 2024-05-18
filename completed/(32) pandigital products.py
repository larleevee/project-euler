#two loops prevents uncesesary iteration

products = set() #no repitition
tbc = set('123456789')

#for single digit multiplicand
for i in range(9): #multiplicand
	for j in range(999,9999): #multiplier (min, max)
		calc = str(i)+str(j)+str(i*j) #must == 9 for true
		if len(calc) == 9 and set(calc) == tbc:
			products.add(i*j)
		elif len(calc) > 9: break #exceeded range for question

#for double digit multiplicand
for i in range(9,99):
	for j in range(99,999):
		calc = str(i)+str(j)+str(i*j)
		if len(calc) == 9 and set(calc) == tbc:
			products.add(i*j)
		elif len(calc)>9: break #exceeded range for question

#printing the result
print(sum(products))