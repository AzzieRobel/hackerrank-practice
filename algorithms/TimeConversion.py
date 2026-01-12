#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    period = s[-2:]
    hh, mm, ss = map(int, s[:-2].split(':'))
    
    if period == 'AM':
        if hh == 12:
            hh = 0
    else:  # PM
        if hh != 12:
            hh += 12
    
    return f"{hh:02d}:{mm:02d}:{ss:02d}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
