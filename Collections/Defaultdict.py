from collections import defaultdict
group_a, group_b = map(int, input().split())
d = defaultdict(list)
for i in range(1, group_a+1):
  d[i].append(str(input()))
for i in range(group_b):
  n = str(input())
  hold_index = []
  for j in d.items():
    if j[1][0]==n:
      hold_index.append(str(j[0]))
  print(" ".join(hold_index) or -1)