# Link --> https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# Code:
def has_cycle(head):
    if head == None:
        return 0
    else:
        slow = head
        fast = head.next
        
        while(slow and fast and fast.next):
            if fast == slow:
                return 1
            fast = fast.next.next
            slow = slow.next
        
        return 0
