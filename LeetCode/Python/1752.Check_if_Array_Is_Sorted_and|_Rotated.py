"""
Problem Statement:
------------------
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 
Otherwise, return false. There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""

# Link --> https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

# Code:
class Solution:
    def check(self, a: List[int]) -> bool:
        # in sorted and sorted-roated array, there exixts only one pair where 
        # current element is smllaer than the previous element
        counter = 0
        
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                counter += 1
        if a[0] < a[len(a) - 1]:
            counter += 1
            
        if counter > 1:
            return False
        else:
            return True
          
          
