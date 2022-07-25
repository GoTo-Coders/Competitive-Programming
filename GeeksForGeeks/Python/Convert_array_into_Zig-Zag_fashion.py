"""
Problem Statement:
------------------
Given an array Arr (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. The converted array should be in form a < b > c < d > e < f. 
The relative order of elements is same in the output i.e you have to iterate on the original array only.

Example 1:
---------
Input:
N = 7
Arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: 3 7 4 8 2 6 1
Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1

Example 2:
---------
Input:
N = 4
Arr[] = {1, 4, 3, 2}
Output: 1 4 2 3
Explanation: 1 < 4 > 2 < 3

Your Task: You don't need to read input or print anything. Your task is to complete the function zigZag() which takes the array of integers arr and n as parameters 
and returns void. You need to modify the array itself. 
NOTE: In the mentioned complexity, only a unique solution will exist.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

# Link --> https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion1638/1

# Code:
class Solution:
	def zigZag(self, a, n):
	    i = 0
	    flag = True       # "Flase" resembles > and "True" resembles <
	    for i in range(len(a)-1):
	        if flag:
    	        if a[i] > a[i+1]:
    	            a[i], a[i+1] = a[i+1], a[i]
    	    else:
    	        if a[i] < a[i+1]:
    	            a[i], a[i+1] = a[i+1], a[i]
    	            
    	    flag = bool(1 - flag)
          
          

