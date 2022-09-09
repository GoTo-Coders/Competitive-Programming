"""
Problem Statement:
------------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
  - Open brackets must be closed by the same type of brackets.
  - Open brackets must be closed in the correct order.
  - Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
----------
Input: s = "()"
Output: true
Example 2:
----------
Input: s = "()[]{}"
Output: true
Example 3:
----------
Input: s = "(]"
Output: false
 
Constraints:
  - 1 <= s.length <= 104
  - s consists of parentheses only '()[]{}'.
"""

# Link --> https://leetcode.com/problems/valid-parentheses/

# Code:
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
       
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif stack:                
                if i == ')' and stack[-1] != '(':
                    return False
                elif i == '}' and stack[-1] != '{':
                    return False
                elif i == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                    return False
        if stack:
            return False
        else:
            return True


