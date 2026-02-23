#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Remove duplicates while preserving descending order
    unique_ranked = []
    for score in ranked:
        if not unique_ranked or unique_ranked[-1] != score:
            unique_ranked.append(score)
    
    result = []
    i = len(unique_ranked) - 1
    
    for p in player:
        while i >= 0 and p >= unique_ranked[i]:
            i -= 1
        result.append(i + 2)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
