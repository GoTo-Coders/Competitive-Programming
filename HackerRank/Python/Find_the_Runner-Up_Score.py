# Link --> https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Code:
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    second_max = 0
    max_no = max(arr)

    for i in arr:
        if i > second_max and i < max_no:
            second_max = i

    print(second_max)

# OTHER WAY:

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    print(arr[arr.index(max(arr)) - 1])
