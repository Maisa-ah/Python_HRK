from collections import Counter
len_arr = int(input())
arr = list(map(int, input().split()))
num_customers = int(input())
count_shoes = Counter(arr)
total_price = 0
for _ in range(num_customers):
  size, price = map(int, input().split())
  if size in count_shoes and count_shoes[size]!=0:
    total_price += price
    count_shoes[size] -= 1
print(total_price)
