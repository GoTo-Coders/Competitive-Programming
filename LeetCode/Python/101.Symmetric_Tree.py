"""
Problem Statement:
------------------
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
----------
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
----------
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Link --> https://leetcode.com/problems/symmetric-tree/

# Code:
def solve(root1, root2):
    if root1 is None and root2 is None:
        return True
        
    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            return solve(root1.left, root2.right) and solve(root1.right, root2.left)
    return False
    
    
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return solve(root, root)
