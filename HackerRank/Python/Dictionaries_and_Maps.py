# Link --> https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Code:
x = int(input())

dictt = {}
for i in range(x):
    user = input().split()
    dictt[user[0]] = user[1]

while True:
    try:
        query = input()
        if query in dictt:
            print(query + "=" + dictt[query])
        else:
            print("Not found")
    except EOFError:
        break
