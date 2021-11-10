# Link --> https://www.hackerrank.com/challenges/whats-your-name/problem

# Code:
def print_full_name(first, last):
    answer_string = "Hello "
    answer_string += (first + " " + last)
    answer_string += "! You just delved into python."
    
    print(answer_string)
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
