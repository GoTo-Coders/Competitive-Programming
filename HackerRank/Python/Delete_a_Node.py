# Link --> https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

# Code:
def deleteNode(head, position):
    if head and position != 0:
        currentNode = head
        while position > 1 and currentNode:
            currentNode = currentNode.next
            position -= 1
            
        currentNode.next = currentNode.next.next
        
        return head
    else:
        return head.next  
