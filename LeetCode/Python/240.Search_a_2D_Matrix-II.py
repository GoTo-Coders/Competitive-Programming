"""
Problem Statement:
------------------
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right. Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""

# Link --> https://leetcode.com/problems/search-a-2d-matrix-ii/

# Code:
class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        rows = len(a)
        cols = len(a[0])
        
        startingRow = 0
        endingCol = cols - 1
        
        while startingRow < rows and endingCol >= 0:
            current_element = a[startingRow][endingCol]
            
            if current_element == target:
                return True
            elif current_element < target:
                startingRow += 1
            else:
                endingCol -= 1
                
        return False
      
