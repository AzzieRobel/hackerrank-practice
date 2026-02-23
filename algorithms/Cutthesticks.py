#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    result = []
    
    while len(arr) > 0:
        # Add the number of sticks before the cut
        result.append(len(arr))
        
        # Find the smallest stick
        min_value = min(arr)
        
        # Cut all sticks by the smallest value
        arr = [x - min_value for x in arr if x - min_value > 0]
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
