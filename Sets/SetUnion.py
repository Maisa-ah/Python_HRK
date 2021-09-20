# Enter your code here. Read input from STDIN. Print output to STDOUT
first = int(input())
set1 = set(map(int, input().split()))
second = int(input())
set2 = set1.union(set(map(int, input().split())))
print(len(set2))
