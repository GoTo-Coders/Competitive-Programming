"""
Problem Statement:
------------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example 1:
----------
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
----------
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
----------
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
-----------
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

# Link: https://leetcode.com/problems/two-sum/description/

# Code:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        # O(N^2) Approach:
        answer = []
        for i in range(len(nums)-1):
            answer.clear()
            answer.append(i)
            for j in range(i+1, len(nums)):
                if nums[j] == (target - nums[i]):
                    answer.append(j)

            if len(answer) == 2:
                break

        return answer
        """

        # O(N) i.e. hash_table approach:
        hash_table = {}

        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in hash_table:
                return [hash_table[remaining], i]

            # filling the number in hash_table (number-index form)
            hash_table[num] = i

        return []
