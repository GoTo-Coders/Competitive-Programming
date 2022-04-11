"""
Problem Statement:
------------------
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# Link --> https://leetcode.com/problems/spiral-matrix/

# Code:
class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        answer = []
        row = len(a)
        col = len(a[0])
        
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
            
