"""
Problem Statement:
------------------
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
----------
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
----------
Input: nums = [0]
Output: [[],[0]]
 

Constraints:
-----------
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""

# Link --> https://leetcode.com/problems/subsets/

# Code:
class Solution:
    def subsetrecursive(self, nums, i, currentResult, answer):
        if i == len(nums):
            answer.append(currentResult)
            return
        
        self.subsetrecursive(nums, i+1, currentResult, answer)
        self.subsetrecursive(nums, i+1, currentResult+[nums[i]], answer)
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.subsetrecursive(nums, 0, [], answer)
        return answer
      
