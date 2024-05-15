def ifDiv(num):
    for i in [11, 13, 14, 16, 17, 18, 19, 20]: #removed all int // into these <-
        if num%i != 0: #my logic: if can be //4, then can be //16?
            return False
    return True

num = 1
while True:
    if ifDiv(num):
        break
    num += 1 #if it fits, count +1

print(num)