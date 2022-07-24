"""
Problem Statement:
-----------------
Given an array arr of n elements which is first increasing and then may be decreasing, find the maximum element in the array.
Note: If the array is increasing then just print then last element will be the maximum value.

Example 1:
---------
Input: 
n = 9
arr[] = {1,15,25,45,42,21,17,12,11}
Output: 45
Explanation: Maximum element is 45.

Example 2:
---------
Input: 
n = 5
arr[] = {1, 45, 47, 50, 5}
Output: 50
Explanation: Maximum element is 50.

Your Task:  You don't need to read input or print anything. Your task is to complete the function findMaximum() which takes the array arr[], 
and n as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)
"""

# Link --> https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1

# Code:
class Solution:

	def findMaximum(self, arr, n):
	    answer = -99999
		for i in arr:
		    if i > answer:
		        answer =  i
		        
		return answer
  
  
