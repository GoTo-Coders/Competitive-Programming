"""
Problem Statement:
------------------
A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks. You may imagine that nums[-1] = nums[n] = -∞. 
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

# Link --> https://leetcode.com/problems/find-peak-element/

# Code:
class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        s = 0                   # start or low
        e = len(a) - 1          # end or high
        
        while s < e:
            mid = s + (e - s) // 2
            
            if a[mid] < a[mid+1]:
                s = mid + 1
            else:
                e = mid
            
        return s
  
