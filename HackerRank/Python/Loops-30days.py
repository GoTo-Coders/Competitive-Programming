# Link --> https://www.hackerrank.com/challenges/30-loops/problem

# Code:
if __name__ == '__main__':
    n = int(input().strip())
    
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)
