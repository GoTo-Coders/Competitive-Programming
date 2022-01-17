# Link --> https://www.hackerrank.com/challenges/30-sorting/problem

# Code:
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    swap_count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                swap_count += 1
                
    print(f"Array is sorted in {swap_count} swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a) - 1]))
