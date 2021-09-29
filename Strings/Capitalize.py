#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
  return " ".join(map(str.capitalize, s.split(' ')))
  # s_list = list(map(str, s.split()))
  # for i in s_list:
  #     if i[0].isalpha():
  #         s_list[s_list.index(i)] = i[0].upper() + i[1:].lower()
  # # print(s_list)
  # # if(first_name[0].isalpha()):
  # #     first_name = first_name[0].upper() + first_name[1:]
  # # if(last_name[0].isalpha()):
  # #     last_name = last_name[0].upper() + last_name[1:]
  # # return first_name + " " + last_name
  # return " ".join(s_list)

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  s = input()

  result = solve(s)

  fptr.write(result + '\n')

  fptr.close()