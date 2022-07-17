"""
Problem Statement:
-----------------
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 
Example 1:
----------
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
----------
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
----------
Input: nums = [1]
Output: [[1]]
 
Constraints:
------------
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""


# Link --> https://leetcode.com/problems/permutations/

# Code:
class Solution:
    def helper(self, s, answer, index):
        # handling the base case.
        if index >= len(s):
            if len(s) > 0:
                answer.append(s.copy())
            return

        for i in range(index, len(s)):
            # swapping the current character.
            s[index], s[i] = s[i], s[index]

            # recursively solving rest.
            self.helper(s, answer, index+1)

            # backtracking.
            s[index], s[i] = s[i], s[index]
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        index = 0
        self.helper(nums, answer, index)
        return answer
      
