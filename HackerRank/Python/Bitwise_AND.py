# Link --> https://www.hackerrank.com/challenges/30-bitwise-and/problem

# Code:
def bitwiseAnd(n, k):
    maximum = 0
    for i in range(1, n+1):
        for j in range(1, i):
            current_answer = i & j
            if maximum < current_answer < k:
                maximum = current_answer
            if maximum == k - 1:
                return maximum
    return maximum
