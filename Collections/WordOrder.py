from collections import Counter
n = int(input())
arr = []
for _ in range(n):
    arr.append(str(input()))
new_dict = Counter(arr)
print(len(new_dict))
for i in new_dict:
    print(new_dict[i], end=" ")

# print(list(new_dict.values()))
