"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
----------
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
---------
Input: nums = [], target = 0
Output: [-1,-1]
"""

# Link --> https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

# Code:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        n = len(nums)
        first = -1
        last = -1
        
        while low < n:
            if nums[low] == target:
                first = low
                break
            low += 1
            
        while high >= 0:
            if nums[high] == target:
                last = high
                break
            high -= 1
            
        return [first, last]
