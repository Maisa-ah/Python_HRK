def merge_the_tools(string, k):
  # 0:3, 3:6, 6:9
  # for i in range(1,k+1):
  #     hold = string[(k*(i-1)):k*i]
  #     arr = []
  #     for j in hold:
  #         if j not in arr:
  #             arr.append(j)
  #     # set_s = set(list(hold))
  #     print(''.join(arr))
  arr=[]
  for i in range(len(string)):
    if string[i] not in arr:
      arr.append(string[i])
      # print(string[i],arr)
    if len(string[:(i+1)])%k==0:
      print(''.join(arr))
      arr=[]
          

if __name__ == '__main__':
  string, k = input(), int(input())
  merge_the_tools(string, k)