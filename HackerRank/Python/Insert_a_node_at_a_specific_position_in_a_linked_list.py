# Link --> https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

# Code:
def insertNodeAtPosition(head, data, position):
    newNode = SinglyLinkedListNode(data)
    if position == 0:
        head = newNode
    else:
        currentNode = head
        
        while position > 1 and currentNode != None:
            currentNode = currentNode.next
            position -= 1
        
        newNode.next = currentNode.next
        currentNode.next = newNode
        
    return head
