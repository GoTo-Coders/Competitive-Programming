"""
Problem Statement:
-----------------
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
---------
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
----------
Input: n = 1
Output: ["()"]
 
Constraints: 1 <= n <= 8
"""

# Link --> https://leetcode.com/problems/generate-parentheses/

# Code:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solveRecursive(n, difference, combination, cobinations):
            # If the difference between the string combination is less than 0.
            # We don't add the combination to the combinations array.
            if difference < 0 or difference > n:
                return
            
            # If the n becomes zero, we can add the current combination,
            # to the combinations array.
            elif n == 0:
                if difference == 0:
                    combinations.append(''.join(combination))
            # Forming combinations recursively.
            else:
                combination.append('(')
                solveRecursive(n - 1 , difference + 1, combination, combinations)
                # Backtracking:
                combination.pop()
                
                combination.append(')')
                solveRecursive(n - 1 , difference - 1, combination, combinations)
                # Backtracking:
                combination.pop()
        
        combinations = []
        solveRecursive(2 * n, 0, [], combinations)
        
        return combinations
