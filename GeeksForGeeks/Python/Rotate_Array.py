"""
Problem Statement:
------------------
Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 

Example 1:
Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.

Example 2:
Input:
N = 10, D = 3
arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20 when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
 
Your Task: Complete the function rotateArr() which takes the array, D and N as input parameters and rotates the array by D elements. 
The array must be modified in-place without using extra space. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

# Link --> https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/#

# Code:
class Solution:
    def rotateArr(self, a, d, n):
        d %= n
        
        a[0:d] = reversed(a[0:d])
        a[d:n] = reversed(a[d:n])
        a[0:n] = reversed(a[0:n])
        
