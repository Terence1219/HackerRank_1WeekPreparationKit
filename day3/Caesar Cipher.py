#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    dict = {}
    for i in range(ord('a'),ord('z')+1):
        dict[chr(i)] = chr((i-ord('a')+k)%(ord('z')-ord('a')+1) + ord('a'))
    for i in range(ord('A'),ord('Z')+1):
        dict[chr(i)] = chr((i-ord('A')+k)%(ord('Z')-ord('A')+1) + ord('A'))
    ans_s = ''
    for alphabet in s:
        if(alphabet in dict):
            ans_s += dict[alphabet]
        else:
            ans_s += alphabet
    return ans_s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
