"""
Problem Statement:
------------------
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
""""

# Link --> https://leetcode.com/problems/search-a-2d-matrix/

# Code:
class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        rows = len(a)
        cols = len(a[0])
        s = 0
        e = (rows * cols) - 1
        
        while s <= e:
            mid = s + (e - s) // 2
            
            mid_element = a[mid // cols][mid % cols]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                s = mid + 1
            else:
                e = mid - 1
                
        return False
      
