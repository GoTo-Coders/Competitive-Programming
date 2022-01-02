# Link --> https://www.hackerrank.com/challenges/itertools-product/problem

# Code:
from itertools import product

a = input().split()
a = list(map(int,a))

b = input().split()
b = list(map(int, b))

products = list(product(a, b))
for i in products:
    print(i, end = " ");
