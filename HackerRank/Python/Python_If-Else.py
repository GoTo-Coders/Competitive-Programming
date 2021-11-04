// Link --> https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

// Code:
def check_even_odd(n):
    if n % 2 != 0 or (n % 2 == 0 and n in range(6, 21)):
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    check_even_odd(n)
