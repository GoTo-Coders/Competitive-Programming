"""
Problem Statement:
-----------------
Given an array of length N consisting of only 0s and 1s in random order. Modify the array to segregate 0s on left side and 1s on the right side of the array.

Example 1:
Input:
N = 5
arr[] = {0, 0, 1, 1, 0}
Output: 0 0 0 1 1

Example 2:
Input:
N = 4
Arr[] = {1, 1, 1, 1}
Output: 1 1 1 1
Explanation: There are no 0 in the given array, 
so the modified array is 1 1 1 1.

Your Task: You don't need to read input or print anything. Your task is to complete the function segregate0and1() which takes arr[] and n as input parameters 
and modifies arr[] in-place without using any extra memory.
"""

# Link --> https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1/#

# Code:
class Solution:
    def segregate0and1(self, a, n):
        left = 0
        right = len(a) - 1
        
        while left < right:
            while(a[left] == 0 and left < right):
                left += 1
            
            while(a[right] == 1 and left < right):
                right -= 1
            
            a[left], a[right] = a[right], a[left]
            left +=1 
            right -= 1
