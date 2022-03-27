"""
Problem Statement:
------------------
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit 
integer range [-231, 231 - 1], then return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

# Link --> https://leetcode.com/problems/reverse-integer/

# Code:
class Solution:
    def reverse(self, x: int) -> int:
        if type(x) is not int:
            return 0
        
        n = abs(x)
        answer = 0
        
        while n != 0:
            remainder = n % 10            
            n = n // 10
            
            answer = ((answer * 10) + remainder)
        
        #  checkimg boundary conditions:
        if answer >= 2 ** 31 - 1 or answer <= -2 ** 31:
            return 0
        elif x < 0:
            return answer * (-1)
        return answer
