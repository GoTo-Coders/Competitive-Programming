# Link --> https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

# Code:
def height(root):
    if root is None:    
        return -1
    
    left_height =  height(root.left) 
    right_height = height(root.right)
    
    return max(left_height , right_height) + 1
