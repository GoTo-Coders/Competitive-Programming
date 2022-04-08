"""
Problem Statement:
------------------
Given a single sentence s, check if it is a palindrome or not. Ignore white spaces and any other character you may encounter. 

Example 1:
Input:
s = race car.
Output: 1 
Explanation: processing str gives us "racecar" which is a palindrome.

Example 2:
Input:
s = hello world.
Output: 0
Explanation: processing str gives us "helloworld" which is not a palindrome.

Your Task: You dont need to read input or print anything. Complete the function sentencePalindrome() which takes a string s as input parameter and 
returns a boolean value denoting if sentence is a palindrome or not.

Note: The driver code prints 1 if the returned value is true, otherwise 0.

Expected Time Complexity: O(N) where N is length of s.
Expected Auxiliary Space: O(1)
"""

# Link --> https://practice.geeksforgeeks.org/problems/string-palindromic-ignoring-spaces4723/1/#Given a single sentence s, check if it is a palindrome or not. Ignore white spaces and any other character you may encounter. 

Example 1:

Input:
s = race car.
Output: 1 
Explanation: processing str gives us
"racecar" which is a palindrome.

Example 2:

Input:
s = hello world.
Output: 0
Explanation: processing str gives us
"helloworld" which is not a palindrome.

Your Task:  
You dont need to read input or print anything. Complete the function sentencePalindrome() which takes a string s as input parameter and returns a boolean value denoting if sentence is a palindrome or not.

Note: The driver code prints 1 if the returned value is true, otherwise 0.


Expected Time Complexity: O(N) where N is length of s.
Expected Auxiliary Space: O(1)



# Code:
def reversedString(s):
    return s[::-1]
    
class Solution:
	def sentencePalindrome(self, s):
		string = []
    
        for i in range(len(s)):
            if s[i].isalnum():     
                string += s[i].lower()
                
        if string == reversedString(string):
            return True
        else:
            return False
