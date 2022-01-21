# Link --> https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Code:
import numpy as np
from scipy import stats

size_of_list = int(input())
xs = []
xs = list(map(int, input().split()))

print(np.mean(xs))
print(np.median(xs))
print(int(stats.mode(xs)[0]))
