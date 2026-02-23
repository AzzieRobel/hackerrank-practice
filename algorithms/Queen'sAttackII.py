#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Top-left diagonal
        (-1, 1),  # Top-right diagonal
        (1, -1),  # Bottom-left diagonal
        (1, 1)    # Bottom-right diagonal
    ]
    
    # Create a set of obstacles for quick lookup
    obstacle_set = set(tuple(obs) for obs in obstacles)
    
    attack_count = 0
    
    # For each direction, check how far the queen can move
    for dr, dc in directions:
        r, c = r_q, c_q
        
        # Move in the current direction until hitting an obstacle or board boundary
        while 1 <= r + dr <= n and 1 <= c + dc <= n:
            r += dr
            c += dc
            if (r, c) in obstacle_set:
                break  # Stop if there's an obstacle
            attack_count += 1
    
    return attack_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
