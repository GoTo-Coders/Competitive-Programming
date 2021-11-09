# Link -->  https://www.hackerrank.com/challenges/finding-the-percentage/problem

# Code:
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    sum = 0
    answer_list = list(student_marks[query_name])
    for i in answer_list:
        sum += i
    
    answer = sum / len(answer_list)
            
    print("%.2f" % answer)
