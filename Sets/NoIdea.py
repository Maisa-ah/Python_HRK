len_arr, len_sets = map(int, input().split())
arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
print(sum([(i in set_a)-(i in set_b) for i in arr]))
# total = 0
# for i in arr:
#     if i in set_a:
#         total += 1
#     if i in set_b:
#         total -= 1
# print(total)