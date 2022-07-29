"""
Problem Statement:
------------------
Given an array A, of N integers A. Return the highest product possible by multiplying 3 numbers from the array.

NOTE:  Solution will fit in a 32-bit signed integer.

Input Format:
The first and the only argument is an integer array A.

Output Format:
Return the highest possible product.

Constraints:
1 <= N <= 5e5

Example:
--------
Input 1:
A = [1, 2, 3, 4]

Output 1:
24

Explanation 1:
2 * 3 * 4 = 24

Input 2:
A = [0, -1, 3, 100, 70, 50]

Output 2:
350000

Explanation 2:
70 * 50 * 100 = 350000
"""

# Link --> https://www.interviewbit.com/problems/highest-product/

# Code:
class Solution:
	def maxp3(self, a):
		a.sort()
		
		answer1 = a[len(a)-1] * a[len(a)-2] * a[len(a)-3]
		
		answer2 = a[0] * a[1] * a[len(a)-1]
		
		return max(answer1, answer2)
  
  
  



