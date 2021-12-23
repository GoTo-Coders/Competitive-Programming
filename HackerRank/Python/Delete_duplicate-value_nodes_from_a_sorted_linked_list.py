# Link --> https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

# Code:
def removeDuplicates(head):
    if head:
        currentNode = head
        
        while currentNode.next:
            if currentNode.data == currentNode.next.data:
                if currentNode.next:
                    currentNode.next = currentNode.next.next
                    continue
            currentNode = currentNode.next
            
    return head
