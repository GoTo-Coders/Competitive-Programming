# Link --> https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

# Code:
def getNode(head, position):
    if not head:
        return None
    if not head.next:
        return head.data
    
    counter = 0
    pointer = head
    while pointer.next:
        counter += 1
        pointer = pointer.next
    head2 = head
    while counter > position:
        head2 = head2.next
        counter -= 1
        
    return head2.data
