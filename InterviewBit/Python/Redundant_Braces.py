"""
Problem Statement:
------------------
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'. Chech whether A has redundant braces or not.

NOTE: A will be always a valid expression.

Problem Constraints
  - 1 <= |A| <= 105

Input Format: The only argument given is string A.
Output Format: Return 1 if A has redundant braces, else return 0.

Example Input
Input 1:
--------
A = "((a+b))"
Input 2:
--------
A = "(a+(a+b))"

Example Output
-------------
Output 1:
1
Output 2:
0


Example Explanation
Explanation 1:
--------------
((a+b)) has redundant braces so answer will be 1.
Explanation 2:
-------------
(a+(a+b)) doesn't have have any redundant braces so answer will be 0.
"""

# Link --> https://www.interviewbit.com/problems/redundant-braces/

# Code:
class Solution:
	def braces(self, s):
        stack = []
        
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                count = 0
                if stack:
                    while stack and stack[-1] != '(':
                        poppedElement = stack.pop()
                        if poppedElement in "+-*/":
                            count += 1
                    stack.pop()
                    
                    if count == 0:
                        return 1
                        
        return 0
      
      








