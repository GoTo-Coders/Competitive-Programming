# Link --> https://www.hackerrank.com/challenges/30-recursion/problem

# Code:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
