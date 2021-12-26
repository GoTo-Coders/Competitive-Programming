# Link --> https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

# Code:
def reverse(head):
    currentNode = head
    nodes = []
    while currentNode:
        nodes.insert(0, currentNode.data)
        currentNode = currentNode.next
    
    newHead = DoublyLinkedList()
    
    for i in range(len(nodes)):
        newHead.insert_node(nodes[i])
    
    return newHead.head
