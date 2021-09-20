if __name__ == '__main__':
  n = int(input())
  arr = map(int, input().split())
  list1 = list(arr)
  print(max([x for x in list1 if x!=max(list1)]))
    
  # get second larger number
  # maxEl = 0

  # if len(list1) == n:
  #   for el in list1:
  #       check = int(el)
  #       if check > maxEl and check!=max(list1):
  #           maxEl = check
  # print(maxEl)
