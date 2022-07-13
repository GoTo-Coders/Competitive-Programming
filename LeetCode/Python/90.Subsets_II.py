"""
Problem Statement:
------------------
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
----------
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
----------
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""

# Link --> https://leetcode.com/problems/subsets-ii/

# Code:
class Solution:
    def solve(self, a, index, currentAnswer, answer):
        if index >= len(a):
            answer.add(tuple(currentAnswer))
            return 
        
        # adding
        self.solve(a, index+1, currentAnswer+[a[index]], answer)
        
        # not adding
        self.solve(a, index+1, currentAnswer, answer)  
        
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        self.solve(nums, 0, [], answer)
        result = []
        
        for i in answer:
            result.append(i)
                
        return result

