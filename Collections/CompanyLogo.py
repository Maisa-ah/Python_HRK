#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
  # sort first to ensure alphabetical order between letters with the same count
    s = Counter(sorted(list(input())))
    # counter_list = list(s.values())
    # print(s.most_common(3))
    # max_vals = [max(counter_list)]
    # for i in range(2):
    #     max_vals.append(max([x for x in counter_list if x!=max(counter_list)]))
    # for i in s:
    #     if s[i] in max_vals:
    #         print(s[i], i)
    # print(s)
    max_list = s.most_common(3)
    # print(max_list)
    for i in s.most_common(3):
        print(i[0],i[1])
        