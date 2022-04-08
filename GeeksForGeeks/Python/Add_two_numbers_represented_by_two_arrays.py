"""
Problem Statement:
------------------
Given two array A[0….N-1] and B[0….M-1] of size N and M respectively, representing two numbers such that every element of arrays represent a digit. 
For example, A[] = { 1, 2, 3} and B[] = { 2, 1, 4 } represent 123 and 214 respectively. The task is to find the sum of both the numbers.

Example 1:
Input : A[] = {1, 2}, B[] = {2, 1}
Output : 33
Explanation: 
N=2, and A[]={1,2}
M=2, and B[]={2,1}
Number represented by first array is 12.
Number represented by second array is 21.
Sum=12+21=33

Example 2:
Input : A[] = {9, 5, 4, 9}, B[] = {2, 1, 4} 
Output : 9763 

Your Task: This is a function problem. The input is already taken care of by the driver code. You only need to complete the function calc_Sum() that takes 
an array (a), sizeOfArray (n), an array (b), sizeOfArray (m), and return the sum . The driver code takes care of the printing.

Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(N + M).
"""

# Link --> https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-two-arrays2408/1/

# Code:
class Solution:
    def calc_Sum (self, a, n, b, m) : 
        sum = []
        i = n - 1
        j = m - 1
        carry = 0
        
        while i >= 0 and j >= 0:
            current_sum = a[i] + b[j] + carry
            carry = current_sum // 10
            current_sum = current_sum % 10
            sum.insert(0, str(current_sum))
            i -= 1
            j -= 1
        
        #  When first array is not traversed completely:
        while i >= 0:
            current_sum = a[i] + carry
            carry = current_sum // 10
            current_sum = current_sum % 10
            sum.insert(0, str(current_sum))
            i -= 1
        
        
        #  When first array is not traversed completely:
        while j >= 0:
            current_sum = b[j] + carry
            carry = current_sum // 10
            current_sum = current_sum % 10
            sum.insert(0, str(current_sum))
            j -= 1
        
        
        #  When there is carry left:
        while carry != 0:
            current_sum = carry
            
            carry = current_sum // 10
            current_sum = current_sum % 10
    
            sum.insert(0, str(current_sum))
        
        
        answer =  "".join(sum)
        answer = int(answer)
        
        return answer
      
