"""
Given a sorted array having N elements, find the indices of the first and last occurrences of an element X in the given array.
Note: If the number X is not found in the array, return '-1' as an array.

Example 1:
----------
Input:
N = 4 , X = 3
arr[] = { 1, 3, 3, 4 }
Output:
1 2
Explanation: For the above array, first occurence of X = 3 is at index = 1 and last occurence is at index = 2.

Example 2:
----------
Input:
N = 4, X = 5
arr[] = { 1, 2, 3, 4 }
Output:
-1
Explanation: As 5 is not present in the array, so the answer is -1.

Your Task: You don't need to read input or print anything. Complete the function firstAndLast() that takes the array arr, its size N and the value X as input parameters
and returns a list of integers containing the indices of first and last occurence of X.

Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)
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
