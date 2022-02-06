# Link --> https://www.hackerrank.com/challenges/py-set-difference-operation/problem

# Code:
n = int(input())
english = set(map(int,input().split()))
m = int(input())
french = set(map(int,input().split()))

print(len(english - french))
