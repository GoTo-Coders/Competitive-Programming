# Link --> https://www.hackerrank.com/challenges/sparse-arrays/problem

# Code:
def matchingStrings(strings, queries):
    answer = []
    for i in range(len(queries)):
        counter = 0
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                counter += 1
        answer.append(counter)
        
    return answer
