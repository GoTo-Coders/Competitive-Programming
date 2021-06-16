/*
Problem Statement:
-----------------
The count-and-say sequence is a sequence of digit strings defined by the recursive formula : countAndSay(1) = "1"

countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string. To determine how you "say" 
a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character.  Then for each group, 
say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Example 1:
---------
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
---------
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 
Constraints:
-----------
1 <= n <= 30
*/

// Link --> https://leetcode.com/problems/count-and-say/

// Code:
class Solution {
public:
    string countAndSay(int n) 
    {
        string output = "11";
        if(n == 1)
           output = "1";
        
        else if(n == 2)
            output = "11";
        
        for(int i=3 ; i<=n ; i++)
        {
            int count = 1;
            string temp;
            
            for(int j=1 ; j<=output.length() ; j++)
            {
                if(output[j] ==output[j-1])
                    count++;
                else
                {
                    temp = temp + to_string(count);
                    temp = temp + output[j-1];
                    count = 1;
                }
            }
            output = temp;
        }
        return output;
    }
};

