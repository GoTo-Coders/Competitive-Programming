# Link --> https://www.hackerrank.com/challenges/python-string-split-and-join/problem

# Code:
def split_and_join(line):
    answer_string = ""
    temp_list = line.split(" ")
    
    for i in range(len(temp_list)):
        answer_string += temp_list[i]
        if i != (len(temp_list)-1):
            answer_string += "-"
    
    return answer_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
