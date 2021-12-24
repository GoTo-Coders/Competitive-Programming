# Link --> https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

# Code:
def sortedInsert(head, data):
    cur = head
    node = DoublyLinkedListNode(data)
    if cur.data > data or cur.data == data:
        node.next = cur
        cur.prev = node
        head = node
        return head
    
    while cur.next:
        if (cur.data < data and cur.next.data > data) or (cur.data == data):
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node
            return head
        cur = cur.next
        
    if cur.data < data or cur.data == data:
        node.prev = cur
        cur.next = node
        return head
