# Link --> https://www.hackerrank.com/challenges/30-review-loop/problem

# Code:
n = int(input())

while n:
    n -= 1
    
    string = input()
    even = ""
    odd = ""
    for i in range(len(string)):
        if i % 2 == 0:
            even = even + string[i]
        else:
            odd = odd + string[i]
            
    print(even + " " + odd)
