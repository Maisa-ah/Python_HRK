test_cases = int(input())
for _ in range(test_cases):
  len_s1 = int(input())
  set_a = set(map(int, input().split()))
  len_s2 = int(input())
  set_b = set(map(int, input().split()))
  diff_set = set_b.intersection(set_a)
  # print(diff_set)
  if len(diff_set)!=len_s1:
    print("False")
  else:
    print("True")
    