# Link --> https://www.hackerrank.com/challenges/arrays-ds/problem

# Code:
import math
import os
import random
import re
import sys

def reverseArray(a):
    n = len(a)
    for i in range(n//2):
        a[i] , a[n-i-1] = a[n-i-1] , a[i]
        
    return a
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
