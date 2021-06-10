#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a_dic, b_dic = {}, {}
    result = 0
    for i in a:
        a_dic[i] = a.count(i)
    for i in b:
        b_dic[i] = b.count(i)
    for key, value in a_dic.items():
        if key in b_dic:
            result += abs(value - b_dic[key])
        elif key not in b_dic:
            result += value
    for key, value in b_dic.items():
        if key not in a_dic:
            result += value 
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
