# Link --> https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

# Code:
def mergeLists(head1, head2):
    head = SinglyLinkedListNode(1)
    answerNode = head
    
    while head1 and head2:
        if head1.data <= head2.data:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next
        
    if head1:
        head.next = head1
        head1 = head1.next
        head = head.next
        
    if head2:
        head.next = head2
        head2 = head2.next
        head = head.next
        
    return answerNode.next
