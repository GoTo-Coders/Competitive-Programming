"""
Problem Statement:
-----------------
Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses.

Example 1:
---------
Input:
N = 3
Output:
((()))
(()())
(())()
()(())
()()()

Example 2:
---------
Input:
N = 1
Output:
()

Your Task: You don't need to read input or print anything. Complete the function AllParenthesis() which takes N as input parameter and returns the list of balanced parenthesis.
"""

# Link --> https://practice.geeksforgeeks.org/problems/generate-all-possible-parentheses/1/

# Code:
class Solution:
    def AllParenthesis(self,n):
        def solveRecursive(n, difference, combination, combinations):
            # If the difference between the string combination is less than 0.
            # We don't add the combination to the combinations array.
            if difference < 0 or difference > n:
                return
            
            # If the n becomes zero, we can add the current combination,
            # to the combinations array.
            elif n == 0:
                if difference == 0:
                    combinations.append(''.join(combination))
            else:
                combination.append('(')
                solveRecursive(n - 1, difference + 1, combination, combinations)
                # Backtracking
                combination.pop()
                
                combination.append(')')
                solveRecursive(n - 1, difference - 1, combination, combinations)
                # Backtracking
                combination.pop()
        
        combinations = []
        solveRecursive(2 * n, 0, [], combinations)
        return combinations
