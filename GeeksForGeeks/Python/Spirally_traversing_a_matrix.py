"""
Problem Statement:
------------------
Given a matrix of size r*c. Traverse the matrix in spiral form.

Example 1:
Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Example 2:
Input:
r = 3, c = 4  
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation: Applying same technique as shown above, output for the 2nd testcase will be 1 2 3 4 8 12 11 10 9 5 6 7.

Your Task: You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, r and c as input parameters and 
returns a list of integers denoting the spiral traversal of matrix. 

Expected Time Complexity: O(r*c)
Expected Auxiliary Space: O(r*c), for returning the answer only.
"""

# Link --> https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1/

# Code:
class Solution:
    def spirallyTraverse(self, a, r, c): 
        answer = []
        row = r
        col = c
        
        startingRow = 0
        startingCol = 0
        endingRow = row - 1
        endingCol = col - 1
        
        # using a count variable to check if we have printed
        # the entire matrix or not.
        total = row * col
        count = 0
        
        while count < total:
            for i in range(startingCol, endingCol + 1):
                if count < total:
                    answer.append(a[startingRow][i])
                    count += 1
            startingRow += 1
            
        
            for i in range(startingRow, endingRow + 1):
                if count < total:
                    answer.append(a[i][endingCol])
                    count += 1
            endingCol -= 1
            
            for i in range(endingCol, startingCol - 1, -1):
                if count < total:
                    answer.append(a[endingRow][i])
                    count += 1
            endingRow -= 1
            
            for i in range(endingRow, startingRow - 1, -1):
                if count < total:
                    answer.append(a[i][startingCol])
                    count += 1
            startingCol += 1
            
        return answer
