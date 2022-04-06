"""
Problem Statement:
------------------
Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

Example 1:
Input:
N = 5
arr[] = {4, 1, 3, 9, 7}
Output:
1 3 4 7 9
Explanation:
Maintain sorted (in bold) and unsorted subarrays.
Select 1. Array becomes 1 4 3 9 7.
Select 3. Array becomes 1 3 4 9 7.
Select 4. Array becomes 1 3 4 9 7.
Select 7. Array becomes 1 3 4 7 9.
Select 9. Array becomes 1 3 4 7 9.

Example 2:
Input:
N = 10
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output:
1 2 3 4 5 6 7 8 9 10

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)
"""

# Link --> https://practice.geeksforgeeks.org/problems/selection-sort/1#

# Code:
class Solution: 
    def selectionSort(self, a,n):
        for i in range(len(a)):
            #taking the current index as minimum index
            minIndex = i
            
            for j in range(i+1, len(a)):
                if a[minIndex] > a[j]:
                    minIndex = j
            # Swapping the current index with minimum value
            a[minIndex], a[i] = a[i], a[minIndex]
            
