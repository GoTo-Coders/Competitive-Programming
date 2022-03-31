"""
Problem Statement:
------------------
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Example 1:
Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation: 0s 1s and 2s are segregated into ascending order.

Example 2:
Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation: 0s 1s and 2s are segregated into ascending order.

Your Task: You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as 
input parameters and sorts the array in-place.
"""

# Link --> https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1/#

# Code:
class Solution:
    def sort012(self, a, n):
        # Approach: 1
        # a.sort()
        # return a
        
        # Approach: 2
        low = 0
        mid = 0
        high = len(a) - 1
        
        while mid <= high:
            if a[mid] == 0:
                a[low], a[mid] = a[mid], a[low]
                low +=1 
                mid += 1
                
            elif a[mid] == 1:
                mid+= 1
            
            else:
                a[mid], a[high] = a[high], a[mid]
                high -= 1
        
        return a
      
