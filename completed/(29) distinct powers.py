sqrs = []

for a in range (2,101):
  for b in range (2,101):
    sqrs.append(a**b)

sqrs.sort()
sqrs = list(dict.fromkeys(sqrs)) #removes all duplicate values (list -> dict -> list)
print(len(sqrs))
