maximum = 1001*1001

nums = [i for i in range(1,maximum+1, 2)]
total = 1
jump = 1
i = 0

while nums[i] != maximum:
    for j in range(4):
        i+= jump
        total += nums[i]
    jump += 1

print(total)
