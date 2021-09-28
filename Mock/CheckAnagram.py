# anagram function with two parameters (type string)

#Summary - originally tried to sort a counter but quickly decided sorting a list was better since count isn't necessary
# it helps to check length first because strings of different lengths cannot be anagrams 

# # from collections import Counter
# # care race
# # war wear
# # Counter({‘c’:1, ‘a’:1, ‘r’:1, ‘e’:1})
# def CheckAnagram(str1, str2):
#   if len(str1) != len(str2):
#     return False
#   else:
#     # count1 = [a, c, e, r]
#     # count2 = [a, c, e, r]
#     count1 = sorted(list(str1))
#     count2 = sorted(list(str2))
#     if(count1 == count2):
#       return True
#     else:
#       return False

# after mock - fixed code to be cleaner
def CheckAnagram(str1, str2):
  if len(str1) == len(str2):
    list1 = sorted(list(str1))
    list2 = sorted(list(str2))
    if(list1 == list2):
      return True
  return False

print(CheckAnagram('race','care'))
print(CheckAnagram('war','wear'))