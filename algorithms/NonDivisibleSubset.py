#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Create a list to store the frequency of remainders
    remainder_count = [0] * k
    
    # Calculate remainders of each element and update the remainder_count
    for num in s:
        remainder_count[num % k] += 1
    
    # We can take at most one element with remainder 0
    count = min(remainder_count[0], 1)
    
    # Iterate through the remainders and count the maximum subset
    for i in range(1, (k // 2) + 1):
        # If k is even and we are at the half-way point, we can only take one element
        if i == k - i:
            count += min(remainder_count[i], 1)
        else:
            # Take the maximum of remainder group i and k-i
            count += max(remainder_count[i], remainder_count[k - i])
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
