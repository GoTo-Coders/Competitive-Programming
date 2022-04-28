"""
Problem Statement:
------------------
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""

# Link --> https://leetcode.com/problems/kth-missing-positive-number/

# Code:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = 0
        i = 1
        missing = []

        while True:
            if i not in arr:
                missing.append(i)
                counter += 1

            if counter > k:
                break
            i += 1

        return missing[k-1]

