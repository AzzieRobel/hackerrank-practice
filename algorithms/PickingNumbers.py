#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Since values are between 0 and 100
    freq = [0] * 101
    
    # Count frequencies
    for num in a:
        freq[num] += 1
    
    max_length = 0
    
    # Check adjacent frequencies
    for i in range(100):
        max_length = max(max_length, freq[i] + freq[i + 1])
    
    return max_length
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
