# Link --> https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

# Code:
def compare_lists(head1, head2):
    if head1 and head2:
        while head1 or head2:
            if (head1 and head2 == None) or (head2 and head1 == None) or (head1.data != head2.data):
                return 0
            head1 = head1.next
            head2 = head2.next
        
        return 1
    
    return 0
