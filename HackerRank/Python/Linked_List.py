# Link --> https://www.hackerrank.com/challenges/30-linked-list/problem

# Code:
def insert(self,head,data):
        newNode = Node(data) 
        # When the list empty
        if head == None:
            head = newNode
        # When there are elements in the list
        else:
            current_Node = head
            while current_Node.next:
                current_Node = current_Node.next
            current_Node.next = newNode
    
        return head
