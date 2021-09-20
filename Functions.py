# Without using any string methods, try to print the following:
# Note that "..." represents the consecutive values in between.

n = int(input())
# without string methods
for i in range(1,n+1):
  print(i,end='')

#with string methods
arr = []
string = ""
for i in range(1,n+1):
  arr.append(str(i))
string = string.join(arr)
print(string)
