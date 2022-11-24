#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    
    stack = []
    bracket = { "(":")", "{":"}", "[":"]" }
    for element in s:
        if element in bracket:
            stack.append(element)
        elif len(stack)==0 or element != bracket[stack.pop()]:
            return "NO"           
    return "NO" if len(stack)!=0 else "YES"

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
