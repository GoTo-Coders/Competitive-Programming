# Link --> https://www.hackerrank.com/challenges/tree-inorder-traversal/problem

# Code:
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)
