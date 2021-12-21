# Link --> https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

# Code:
def reversePrint(head):
    if head:
        reversed = []
        currentNode = head
        
        while currentNode:
            reversed.insert(0,currentNode.data)
            currentNode = currentNode.next
        
        for i in range(len(reversed)):
            print(reversed[i])
