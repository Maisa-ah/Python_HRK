def minion_game(string):
  vowels = ['A', 'E', 'I', 'O', 'U']
  p1 = 0
  p2 = 0
  for i in range(len(string)):
    # print(string[i], len(string)-i)
    if string[i] in vowels:
      p2+=len(string)-i
    else:
      p1+=len(string)-i
  # checked_arr = []
  # for i in range(len(string)+1):
  #     for j in range(len(string)+1):
  #         if len(string[i:j]) > 0:
  #             hold = string
  #             while string[i:j] in hold and string[i:j] not in checked_arr:
  #                 # print("string here ", hold, string[i:j], p1, p2)
  #                 find_index = hold.find(string[i:j])
  #                 hold = hold[:find_index] + hold[find_index+1:]
  #                 if string[i:j][0] in vowels:
  #                     p2 += 1
  #                 else:
  #                     p1 += 1
  #             checked_arr.append(string[i:j])
  if p1 > p2:
    print("Stuart", p1)
  elif p2 > p1:
    print("Kevin", p2)
  else:
    print("Draw")
      
    

if __name__ == '__main__':
  s = input()
  minion_game(s)