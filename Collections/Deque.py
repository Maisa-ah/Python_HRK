# from collections import deque
# n = int(input())
# d = deque()
# for i in range(n):
#     func, *val = input().split()
#     if len(val)>0:
#         getattr(d,func)(val[0])
#     else:
#         getattr(d,func)()
# # print(d.count('1'))
# for i in d:
#     print(i, end=' ')

from collections import deque
n = int(input())
d = deque()
for i in range(n):
  func, *val = input().split()
  getattr(d,func)(*val)
# print(*[i for i in d])
print(*d)
