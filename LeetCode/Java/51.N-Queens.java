/*
Problem Statement:
------------------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
Example 1:
----------
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:
---------
Input: n = 1
Output: [["Q"]]
 
Constraints: 1 <= n <= 9
*/

// Link --> https://leetcode.com/problems/n-queens/

// Code:
class Solution {
    
    public Boolean isSafe(int row, int column, char[][] board) {
        int n = board.length;
        
        // Horizontal Check:
        for(int i=0; i<n; i++) {
            if(board[row][i] == 'Q')
                return false;
        }
        
        // Vertical Check:
        for(int i=0; i<n; i++) {
            if(board[i][column] == 'Q')
                return false;
        }
        
        // Top Left Check: (row decrease, column decrease)
        int r = row;
        for(int c=column; c>=0 && r>=0; r--, c--) {
            if(board[r][c] == 'Q')
                return false;
        }
        
        // Top Right Check: (row decrease, column increase)
        r = row;
        for(int c=column; c<n && r>=0; r--, c++) {
            if(board[r][c] == 'Q')
                return false;
        }
        
        // Bottom Left Check: (row increase, column increase)
        r = row;
        for(int c=column; c>=0 && r<n; r++, c--) {
            if(board[r][c] == 'Q')
                return false;
        }
        
        // Bottom Right Check: (row increase, column increase)
        for(int c=column; c<n && r<n; r++, c++) {
            if(board[r][c] == 'Q')
                return false;
        }
        
        return true;
    }
    
    public void saveBoard(char[][] board, List<List<String>> allBoards) {
        String row = "";
        List<String> newBoard = new ArrayList<>();
        
        for(int i=0; i<board.length; i++) {
            row = "";
            for(int j=0; j<board[0].length; j++) {
                if(board[i][j] == 'Q')
                    row += 'Q';
                else
                    row += '.';
            }
            // adding the row to the board:
            newBoard.add(row);
        }
        // Finally adding the current board to the main board i.e. allBoards
        allBoards.add(newBoard);
    }
    
    public void helper(char[][] board, List<List<String>> allBoards, int column) {
        // Base Case:
        if(column == board.length) {
            saveBoard(board, allBoards);
            return;
        }
        
        // going through all rows in the given column
        for(int row = 0; row < board.length; row++) {
            if(isSafe(row, column, board)) {
                board[row][column] = 'Q';
                
                // After placing we will call recursive function for next column.
                helper(board, allBoards, column + 1); 
                
                // BACKTRACK if the position is incorrect.
                board[row][column] = '.';
            }
            else {
                board[row][column] = '.';
            }
        }
    }
    
    public List<List<String>> solveNQueens(int n) {
        
        List<List<String>> allBoards = new ArrayList<>();
        char[][] board = new char[n][n];
        int startingColumn = 0;
        
        // We will put queens column-wise.
        helper(board, allBoards, startingColumn);
        
        return allBoards;
    }
}
