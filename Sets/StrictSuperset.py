set_a = set(map(int, input().split()))
n = int(input())
check_strict = True
for _ in range(n):
  set_b = set(map(int, input().split()))
  set_c = set_b.difference(set_a)
  if len(set_c)>0:
    check_strict = False
print(check_strict)
        