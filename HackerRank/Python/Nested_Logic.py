# Link --> https://www.hackerrank.com/challenges/30-nested-logic/problem

# Code:
n = input()
returned = list(map(int, n.split()))

m = input()
bought = list(map(int, m.split()))

dues = 0

if bought[2] < returned[2]:
    dues = 10000
elif bought[2] == returned[2]:
    if bought[1] < returned[1]:
        difference = int(returned[1]) - int(bought[1])
        dues = 500 * difference
    elif bought[0] < returned[0]:
        difference = int(returned[0]) - int(bought[0])
        dues = 15 * difference
        
print(dues)
