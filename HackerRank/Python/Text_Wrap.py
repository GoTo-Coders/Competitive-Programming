# Link --> https://www.hackerrank.com/challenges/text-wrap/problem

# Code:
import textwrap

def wrap(s, max_width):
    words = textwrap.TextWrapper(width = max_width)
    word_list = words.wrap(text = s)
    
    final_string = ""
    for i in range(len(word_list)):
        final_string += word_list[i]
        final_string += "\n"
    
    return final_string
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
