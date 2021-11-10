# Link --> https://www.hackerrank.com/challenges/swap-case/problem

# Code:
def swap_case(s):
    answer_string = ""
    for i in s:
        if i.isupper():
            answer_string += i.lower()
        elif i.islower():
            answer_string += i.upper()
        else:
            answer_string += i
    return answer_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
