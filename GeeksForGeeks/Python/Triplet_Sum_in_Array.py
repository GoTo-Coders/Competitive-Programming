"""
Problem Statement:
------------------
Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.

Example 1:
Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation: The triplet {1, 4, 8} in the array sums up to 13.

Example 2:
Input:
n = 5, X = 10
arr[] = [1 2 4 3 6]
Output:
1
Explanation: The triplet {1, 3, 6} in the array sums up to 10.

Your Task: You don't need to read input or print anything. Your task is to complete the function find3Numbers() which takes the array arr[], 
the size of the array (n) and the sum (X) as inputs and returns True if there exists a triplet in the array arr[] which sums up to X and False otherwise.
"""

# Link --> https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1#

# Code:
class Solution:
    def find3Numbers(self,a, n, x):
        a.sort()
        
        for i in range(len(a)):
            left = i + 1
            right = len(a) - 1
            
            while left < right:
                if a[i] + a[left] + a[right] == x:
                    return True
                elif a[i] + a[left] + a[right] < x:
                    left += 1
                else:
                    right -= 1
        
        return False
