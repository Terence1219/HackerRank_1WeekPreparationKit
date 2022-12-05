#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    left = []
    for i in range(len(petrolpumps)):
        left.append(petrolpumps[i][0]-petrolpumps[i][1])
    for i in range(len(left)):
        if left[i] > 0:
            petrol = left[i]
            j = (i + 1) % len(left)
            while(j!=i):
                petrol += left[j]
                if(petrol < 0):
                    break
                j = (j + 1) % len(left)
                if j == i:
                    return i
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
