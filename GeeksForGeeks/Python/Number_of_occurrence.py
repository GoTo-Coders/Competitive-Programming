"""
Problem Statement:
------------------
Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

Example 1:
Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: 2 occurs 4 times in the given array.

Example 2:
Input:
N = 7, X = 4
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 0
Explanation: 4 is not present in the given array.

Your Task: You don't need to read input or print anything. Your task is to complete the function count() which takes the array of integers arr, 
n and x as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
"""

# Link --> https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1/

# Code:
class Solution:
	def count(self, a, n, x):
		# First we will calculate the first and last 
		# occurence of the target eleemnt. We can easily tell
		# the mumber of occurences using first and last occurence.
		
		low = 0
		high = n - 1
		first = -1
		last = -1
		
		while low <= high:
		    if a[low] != x:
		        low +=1
		    elif a[high] != x:
		        high -= 1
		    elif a[low] == x and a[high] == x:
		        first = low
		        last = high
		        break
		    
		if first != -1 and last != -1:
		    return (last - first) + 1
		else:
		    return last - first
