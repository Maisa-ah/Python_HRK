len_set1 = int(input())
set1 = set(map(int, input().split()))
n = int(input())
for _ in range(n):
  user_func, len_set2 = input().split()
  set2 = set(map(int, input().split()))
  # getattr(object,attribute, default)
  getattr(set1, user_func)(set2)
  # if(user_func == 'intersection_update'):
  #     set1.intersection_update(set2)
  # if(user_func == 'update'):
  #     set1.update(set2)
  # if(user_func == 'symmetric_difference_update'):
  #     set1.symmetric_difference_update(set2)
  # if(user_func == 'difference_update'):
  #     set1.difference_update(set2)
print(sum(set1))
        