'''
Problem Statement:
------------------
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
----------
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

# Link --> https://leetcode.com/problems/binary-search/

# Code:
class Solution:
    def search(self, cards: List[int], query: int) -> int:
        position = -1

        if len(cards) == 0:
            return position

        low = 0
        high = len(cards) - 1

        # Binary Search Technique
        while low <= high and high >= low:
            mid = (low + high) // 2

            if cards[mid] == query:
                position = mid
                break

            if cards[mid] <= query:
                low = mid + 1

            else:
                high = mid - 1

        return position
      
