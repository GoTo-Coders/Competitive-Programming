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



# OTHER WAY (without using extra list):
def reverse(head):
    previous = head
    current = head
    
    while current:
        previous = current.prev
        
        # Swapping left and right nodes:
        current.prev = current.next
        current.next = previous
        
        # Finally moving current to rightward:
        current = current.prev
        
    if previous:
        head = previous.prev    
        
    return head
