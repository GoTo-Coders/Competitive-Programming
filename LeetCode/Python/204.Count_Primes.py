"""
Problem Statement:
------------------
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
"""

# Link --> https://leetcode.com/problems/count-primes/

# Code:
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * (n)
    
        prime[:2] = [False, False]
        
        for i in range(2, n):
            if prime[i]:
                # marking all its multiples as non-prime
                j = 2*i
                while j < n:
                    prime[j] = False
                    j += i
                    
        return sum(prime)
    
    
"""
# Other Approach:
        isPrime = [True] * n
        isPrime[:2] = [False, False]
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i: n: i] = [False] * len(isPrime[i * i: n: i])
        return sum(isPrime)
"""
