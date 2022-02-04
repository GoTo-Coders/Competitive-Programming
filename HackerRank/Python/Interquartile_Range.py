# Link --> https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Code:
import math
import os
import random
import re
import sys
import statistics

def interQuartile(values, freqs):
    arr = []
    for i in range(len(freqs)):
        for j in range(freqs[i]):
            arr.append(values[i])
    
    arr.sort()
    arr_len = len(arr)
        
    if arr_len != 0:
        q1 = statistics.median(arr[ : arr_len // 2])
        q3 = statistics.median(arr[(arr_len // 2) + 1 : ])
    else:
        q1 = statistics.median(arr[ : arr_len // 2])
        q3 = statistics.median(arr[arr_len // 2 : ])
        
    print(round(float(q3 - q1), 1))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
