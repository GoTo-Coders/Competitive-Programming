# Link --> https://www.hackerrank.com/challenges/30-binary-numbers/problem

# Code:
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n).replace("0b", "")
    answer = 0
    current_answer = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            current_answer += 1
        else:
            answer = max(answer, current_answer)
            current_answer = 0
        
    print(max(answer, current_answer))
