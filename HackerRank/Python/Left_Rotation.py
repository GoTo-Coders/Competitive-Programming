# Link --> https://www.hackerrank.com/challenges/array-left-rotation/problem

# Code:
import math
import os
import random
import re
import sys

def rotateLeft(d, a):
    total_rotations = d % len(a)
    answer = []
    
    for i in range(d, len(a)):
        answer.append(a[i])
    for i in range(d):
        answer.append(a[i])
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
