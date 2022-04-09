"""
Problem Statement:
-----------------
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:
Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole string(not individual words), the input string becomes much.very.program.this.like.i

Example 2:
Input:
S = pqr.mno
Output: mno.pqr
Explanation: After reversing the whole string , the input string becomes mno.pqr

Your Task: You dont need to read input or print anything. Complete the function reverseWords() which takes string S as input parameter and 
returns a string containing the words in reversed order. Each word in the returning string should also be separated by '.' 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)
"""

# Link --> https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1/#

# Code:
class Solution:
    def reverseWords(self, s):
        s += "."
        answer = []
        string = ""
        for i in range(len(s)):
            string += s[i]
            if s[i] == ".":
                answer.insert(0, string)
                string = ""
                
        result = "".join(answer)
        return result[:len(result)-1]
      
