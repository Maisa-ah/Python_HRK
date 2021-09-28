n = int(input())

for _ in range(n):
  size = int(input())
  arr = list(map(int, input().split()))
  left_most = 0
  right_most = len(arr)-1
  i=0
  while i < right_most and arr[i] >= arr[i+1]: 
    # print((arr[i]),arr[i+1])
    i += 1
  while i < right_most and arr[i] <= arr[i+1]:
    # print((arr[i]),arr[i+1])
    i += 1
  if i == right_most:
    print("Yes") 
  else:
    print("No")
