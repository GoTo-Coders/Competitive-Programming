# Link --> https://www.hackerrank.com/challenges/python-lists/problem

# Code:
if __name__ == '__main__':
    n = int(input())
    
    lst = []
    
    for i in range(n):
        ip = input().split();
        if ip[0] == "print":
            print(lst)
        elif ip[0] == "insert":
            lst.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            lst.remove(int(ip[1]))
        elif ip[0] == "pop":
            lst.pop();
        elif ip[0] == "append":
            lst.append(int(ip[1]))
        elif ip[0] == "sort":
            lst.sort();
        else:
            lst.reverse();
