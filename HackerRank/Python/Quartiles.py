# Link --> https://www.hackerrank.com/challenges/s10-quartiles/problem

# Code:
import math
import os
import random
import re
import sys
import statistics

def quartiles(arr, n):
    arr.sort()
    
    left_arr = arr[: n//2]
    right_arr = arr[(n+1)//2: ]
    
    answer = []
    answer.append(int(statistics.median(left_arr)))
    answer.append(int(statistics.median(arr)))
    answer.append(int(statistics.median(right_arr)))
    
    return answer
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data, n)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
