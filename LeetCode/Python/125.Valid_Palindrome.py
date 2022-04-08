"""
Problem Statement:
------------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.
"""

# Link --> https://leetcode.com/problems/valid-palindrome/

# Code:
def reversedString(s):
    return s[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        string = []
    
        for i in range(len(s)):
            if s[i].isalnum():     
                string += s[i].lower()
                
        if string == reversedString(string):
            return True
        else:
            return False
          
