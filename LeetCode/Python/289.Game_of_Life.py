"""
Problem Statement:
------------------
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. 
Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""

# Link --> https://leetcode.com/problems/game-of-life/

# Code:
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0]) if m else 0
        for i in range(m):
            for j in range(n):
                count = 0
                
                for I in range(max(i-1, 0), min(i+2, m)):
                    for J in range(max(j-1, 0), min(j+2, n)):
                        count += board[I][J] & 1

                if (count == 4 and board[i][j]) or count == 3:
                    board[i][j] |= 2  

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1 
