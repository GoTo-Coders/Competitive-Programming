# Link --> https://www.hackerrank.com/challenges/30-regex-patterns/problem

# Code:
if __name__ == '__main__':
    N = int(input().strip())
    answer = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        if "@gmail.com"in emailID:
            answer.append(firstName)
            
    answer.sort()
    for i in answer:
        print(i)
        
        
