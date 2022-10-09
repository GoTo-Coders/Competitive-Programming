"""
Problem Statement:
------------------
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
 
Example 1:
----------
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
----------
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
---------
Input: s = ""
Output: 0
"""

# Link --> https://leetcode.com/problems/longest-valid-parentheses/

# Code:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        check = [0]*n
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    check[stack.pop()] = 1
                    check[i] = 1
                    
        max_count = 0
        count = 0
        
        for i in range(n):
            if check[i]:
                count += 1
            else:
                count = 0
            max_count = max(max_count, count)
                
                
        return max_count
      
      
