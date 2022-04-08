"""
Problem Statement:
------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

# Link -->

# Code:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        counter = 0
        j = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
                i += 1
                
            else:
                counter += 1
                i += 1
                
        while counter != 0:
            nums[j] = 0
            j += 1 
            counter -= 1
            
