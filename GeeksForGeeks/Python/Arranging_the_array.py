"""
Problem Statement:
------------------
You are given an array of size N. Rearrange the given array in-place such that all the negative numbers occur before positive numbers.
(Maintain the order of all -ve and +ve numbers as given in the original array).
 
Example 1:
---------
Input:
N = 4
Arr[] = {-3, 3, -2, 2}
Output:
-3 -2 3 2
Explanation: In the given array, negative numbers are -3, -2 and positive numbers are 3, 2. 

Example 2:
----------
Input:
N = 5
Arr[] = {2, -4, 7, -3, 4}
Output:
-4 -3 2 7 4
 
Your Task: You don't need to read input or print anything. Your task is to complete the function Rearrange() which takes the array Arr[] and 
its size N as inputs and returns the array after rearranging with spaces between the elements of the array.

Expected Time Complexity: O(N. Log(N))
Expected Auxiliary Space: O(Log(N))
"""

# Link --> https://practice.geeksforgeeks.org/problems/arranging-the-array1131/1

# Code:
def Rearrange(a, n):
    answer = []
    for i in range(n):
        if a[i] < 0:
            answer.append(a[i])
            
    for i in range(n):
        if a[i] >= 0:
            answer.append(a[i])
    
    for i in range(n):
        a[i] = answer[i]
        
