"""
Problem Statement:
------------------
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""

# Link --> https://leetcode.com/problems/unique-number-of-occurrences/

# Code:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        
        for i in arr:
            if i in counts.keys():
                counts[i] = counts[i] + 1
            else:
                counts[i] = 1
        
        frequencies = list(counts.values())
        frequencies.sort()
        
        for i in range(len(frequencies) - 1):
            if frequencies[i] == frequencies[i+1]:
                return False
            
        return True
