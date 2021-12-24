# Link --> https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

# Code:
def findMergeNode(head1, head2):
    while head1:
        currentNode = head2
        while currentNode:
            if head1 == currentNode:
                return head1.data
            currentNode = currentNode.next
        head1 = head1.next
