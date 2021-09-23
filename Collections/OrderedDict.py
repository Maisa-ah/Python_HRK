from collections import OrderedDict
n = int(input())
new_dict = OrderedDict()
for _ in range(n):
    item, price = input().rsplit(" ",1)
    if item in new_dict:
        new_dict[item] = new_dict[item] + int(price)
    else:
        new_dict[item] = int(price)
for key in new_dict:
    print(key,new_dict[key])