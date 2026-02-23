#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Step 1: Count the number of 'a's in the original string `s`
    count_a_in_s = s.count('a')
    
    # Step 2: Determine how many complete repetitions of `s` fit into `n`
    full_repeats = n // len(s)
    
    # Step 3: Calculate the number of 'a's from full repetitions
    total_a_count = full_repeats * count_a_in_s
    
    # Step 4: Handle the remaining part of the string
    remainder = n % len(s)
    
    # Step 5: Count 'a's in the remainder of the string
    total_a_count += s[:remainder].count('a')
    
    return total_a_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
