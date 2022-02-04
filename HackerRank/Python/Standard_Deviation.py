# Link --> https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# Code:
import math
import os
import random
import re
import sys
import statistics

def stdDev(arr):
    n = len(arr)
    
    mean = sum(arr) / n
    variance = sum([((x - mean) ** 2) for x in arr]) / n
    stddev = variance ** 0.5

    print("{0:0.1f}".format(stddev))
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
