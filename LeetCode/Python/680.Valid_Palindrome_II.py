"""
Problem Statement:
------------------
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
"""

# Link --> https://leetcode.com/problems/valid-palindrome-ii/

# Code:
def helper(s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return helper(s, i + 1, j) or helper(s, i, j - 1)
                
        return True
