# Link --> https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

# Code:
def lca(root, v1, v2):
    if root and (root.info == v1 or root.info == v2):
        return root
    
    if  root is None:
        return None

    left = lca(root.left, v1, v2)
    right = lca(root.right, v1, v2)
    
    # IMPORTANT BASE CASES:
    if left is None and right is None:
        return None
    if left and right:
        return root
    else:
        if right is None:
            return left
        else:
            return right
