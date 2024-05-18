def nextPerm(arr):

  #find index of k
  i = len(arr) - 1
  while (i > 0) and (arr[i-1] >= arr[i]):
    i -= 1
  #if i <= 0:
    #print('last permutation =', arr)
    #return arr
  
  #find index of l
  j = len(arr)-1
  while arr[j] <= arr[i-1]:
    j -=1
  
  #swap a[k] and a[l]
  arr[i-1], arr[j] = arr[j], arr[i-1]

  #reverse from a[k+1] up to & including end
  arr[i:] = arr[len(arr) - 1 : i - 1 : -1]
  return arr


arr = [0,1,2,3,4,5,6,7,8,9]

for i in range(0, 1000000-2):
  nextseq = nextPerm(arr)
  arr = nextseq

print(arr)