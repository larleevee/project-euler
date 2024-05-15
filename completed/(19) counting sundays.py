normalYear = [31,28,31,30,31,30,31,31,30,31,30,31] #days of months
leapYear = [31,29,31,30,31,30,31,31,30,31,30,31]#days of months

years = [normalYear] * 100 #all years
for i in range(3, len(years), 4) :
    years[i] = leapYear # every 4th year = leap year

currentDay = 365 % 7 #day at start (sun = day 1)
sundays = 0

for y in years : #year in years
    for m in y : #month in years
        if currentDay % 7 == 6: # 6/7 days in week at end of month, making sun first of next
            sundays += 1
        currentDay += m % 7 #roll over days left

print (sundays)
