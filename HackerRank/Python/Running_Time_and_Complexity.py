# Link --> https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

# Code:
import math
tests = int(input())

def is_prime(num):
    a = 2
    while a<= math.sqrt(num):
        if num % a < 1:
            return False
        a = a + 1
    return num > 1

to_check = []
while tests:
    tests -= 1
    
    to_check.append(int(input()))
    
for i in range(len(to_check)):
    if is_prime(to_check[i]):
        print("Prime")
    else:
        print("Not prime")
