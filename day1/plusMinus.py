#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    zero = 0
    neg = 0
    for a in arr:
        if a > 0:
            pos += 1
        elif a < 0:
            neg += 1
        else:
            zero += 1
    print('%.6f'%(pos/len(arr)))
    print('%.6f'%(neg/len(arr)))
    print('%.6f'%(zero/len(arr)))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
