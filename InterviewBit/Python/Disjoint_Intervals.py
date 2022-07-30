"""
Problem Statement:
------------------
Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.
Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.
Return a integer denoting the length of maximal set of mutually disjoint intervals.

Problem Constraints
1 <= N <= 105
1 <= A[i][0] <= A[i][1] <= 109

Input Format
First and only argument is a 2D array A of size N x 2 denoting the N intervals.

Output Format
Return a integer denoting the length of maximal set of mutually disjoint intervals.

Example Input
Input 1:
A = [
       [1, 4]
       [2, 3]
       [4, 6]
       [8, 9]
     ]
     
Input 2:
 A = [
       [1, 9]
       [2, 3]
       [5, 7]
     ]
     
Example Output
Output 1:
 3
 
Output 2:
 2

Example Explanation
-------------------
Explanation 1:
 Intervals: [ [1, 4], [2, 3], [4, 6], [8, 9] ]
 Intervals [2, 3] and [1, 4] overlap.
 We must include [2, 3] because if [1, 4] is included thenwe cannot include [4, 6].
 We can include at max three disjoint intervals: [[2, 3], [4, 6], [8, 9]]
 
Explanation 2:
 Intervals: [ [1, 9], [2, 3], [5, 7] ]
 We can include at max two disjoint intervals: [[2, 3], [5, 7]]
"""

# Link --> https://www.interviewbit.com/problems/disjoint-intervals/

# Code:
class Solution:
    def solve(self, a):
        a.sort(key=lambda x: x[1])
        
        count = 1
        start, end = a[0]
        
        for currentStart, currentEnd in a:
            if currentStart > end:
                count += 1
                
                start, end = currentStart, currentEnd
                
        
        return count
      
      


