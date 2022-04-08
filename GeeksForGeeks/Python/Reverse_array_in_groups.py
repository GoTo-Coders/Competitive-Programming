"""
Problem Statement:
------------------
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

Example 1:
Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.

Example 2:
Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9

Your Task: You don't need to read input or print anything. The task is to complete the function reverseInGroups() which takes the array, N and K as 
input parameters and modifies the array in-place. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""

# Link --> https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1/

# Code:
class Solution:	
	def reverseInGroups(self, a, n, k):
		i = 0
     
        while i < n:
            l = i
            r = min(i + k - 1, n - 1)
     
            while (l < r):
                a[l], a[r] = a[r], a[l]
                l += 1;
                r -= 1
                
            i += k
