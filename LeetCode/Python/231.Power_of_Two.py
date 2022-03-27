"""
Problem Statement:
------------------
Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
"""

# Link --> https://leetcode.com/problems/power-of-two/

# Code:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = bin(n).replace("0b","")
        if m.count('1') == 1 and n > 0:
            return True
        else:
            return False
        
        
        """
        # Non-optimized:
        def isPowerOfTwo(self, n: int) -> bool:
        # base cases:
        if n == 1:
            return True
        elif n % 2 != 0:
            return False
        else:
            flag = False
            upper_limit = 30
            for i in range(1, upper_limit):
                # check = pow(2, i)
                if pow(2, i) == n:
                    flag = True
                    break

            return flag
        """
