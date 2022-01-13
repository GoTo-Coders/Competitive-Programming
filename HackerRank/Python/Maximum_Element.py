# Link --> https://www.hackerrank.com/challenges/maximum-element/problem

# Code:
def getMax(operations):
    maximum = 0
    temp = []
    answer = []
    
    for i in operations:
        if i != '2' and i != '3':
            numbers = i.split()
            number = int(numbers[1])
            temp.append(number)
            if number > maximum:
                maximum = number
        elif i == '2':
            temp.pop()
            if len(temp) != 0:
                maximum = max(temp)
            else:
                maximum = 0
        else:
            answer.append(maximum)
    
    return answer
