"""
Problem Statement:
------------------
Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements appear exactly twice. 

Example 1:
Input:
N = 11
arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65}
Output: 4
Explanation: 4 is the only element that appears exactly once.
 
Your Task: You don't need to read input or print anything. Complete the function findOnce() which takes sorted array and its size as its input parameter 
and returns the element that appears only once. 

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)
"""

# Link --> https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/

# Code:
class Solution:
    def findOnce(self, a : list, n : int):
        if len(a) == 1:
            return a[0]
            
        i = 0
        
        while i < len(a) - 1:
            if a[i] == a[i+1]:
                i += 2
            else:
                return a[i]
        
                
        return a[len(a) - 1]
      
      
