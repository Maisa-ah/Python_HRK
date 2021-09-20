len_a = int(input())
set_a = set(map(int, input().split()))
len_b = int(input())
set_b = set(map(int, input().split()))
set_c = sorted(set_a.symmetric_difference(set_b))
for i in set_c:
  print(i)