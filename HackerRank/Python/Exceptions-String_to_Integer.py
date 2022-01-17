# Link --> https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

# Code:
import sys

S = input().strip()
try:
    S = int(S)
    print(S)
except:
    print("Bad String")
