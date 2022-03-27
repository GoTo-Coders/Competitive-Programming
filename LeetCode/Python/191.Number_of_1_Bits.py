# Link --> https://leetcode.com/problems/number-of-1-bits/submissions/

# Code:
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while (n):
            count += n & 1
            n >>= 1
            
        return count
    
    """
    # Other way
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        return binary.count('1')
    """
