/*
Problem Statement:
------------------
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
---------
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
---------
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
Constraints:
-----------
1 <= s.length <= 105
s[i] is a printable ascii character.
*/

// Link --> https://leetcode.com/problems/reverse-string/

//Code:
class Solution 
{
public:
    void reverseString(vector<char>& s) 
    {
        int n = s.size();
        for(int i=0 ; i<n/2 ; i++)
        {
            char temp = s[i];
            s[i] = s[n-i-1];
            s[n-i-1] = temp;
        }
    }
};
