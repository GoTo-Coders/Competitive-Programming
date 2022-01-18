# Link --> https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

# Code:
def removeDuplicates(self,head):
        if head:
            current = head
            while current:
                if current.next and current.next:
                    if current.data == current.next.data:
                        current.next = current.next.next
                        continue
                current = current.next
                    
        return head
