# Link --> https://www.hackerrank.com/challenges/tree-postorder-traversal/problem

# Code:
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=" ")
