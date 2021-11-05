# Link --> https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

# Code:
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input()) 
    
    answer_list = []
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    answer_list.append([i, j, k])
    
    print(answer_list)
