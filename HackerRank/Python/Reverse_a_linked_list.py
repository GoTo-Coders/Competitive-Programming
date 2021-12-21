# Link --> https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

# Code:
def reverse(head):
    if head:
        reversed = []
        currentNode = head
        
        while currentNode:
            reversed.insert(0,currentNode.data)
            currentNode = currentNode.next
        
        newHead = SinglyLinkedList()
        for i in range(len(reversed)):
            newHead.insert_node(reversed[i])
        
        return newHead.head
