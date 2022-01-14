# Link --> https://www.hackerrank.com/challenges/30-arrays/problem

# Code:
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    for i in range(len(arr)):
        print(arr[len(arr) - i - 1], end=" ")
