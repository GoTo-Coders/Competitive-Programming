# Link --> https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

# Code:
def preOrder(root):
    if root:
        print(root.info, end=" ")
        preOrder(root.left)
        preOrder(root.right)
