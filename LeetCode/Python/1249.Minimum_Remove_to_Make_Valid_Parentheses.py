"""
Problem Statement:
-----------------
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
  - It is the empty string, contains only lowercase characters, or
  - It can be written as AB (A concatenated with B), where A and B are valid strings, or
  - It can be written as (A), where A is a valid string.
 

Example 1:
---------
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
----------
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
----------
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
------------
  - 1 <= s.length <= 105
  - s[i] is either'(' , ')', or lowercase English letter.
"""

# Link --> https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Code:
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        # a stack that will contain 1 for valid parenthesis and 0 for invalid one.
        # initially we are supposing that all the parenthesis are invalid.
        check = [0]*len(s)
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    # marking the top element as valid one and then popping it.
                    check[stack.pop()] = 1
                    # marking its corresponding (the current index) as valid one.
                    check[i] = 1
                    
        # defining an empty string to store the result.
        answer = ""
        
        for i, c in enumerate(s):
            if c in '()':
                # checking if the current index contains the valid parenthesis or not.
                if check[i]:
                    answer += c
            else:
                answer += c
                    
        return answer





