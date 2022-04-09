/*
Problem Statement:
------------------
Bingu was testing all the strings he had at his place and found that most of them were prone to a vicious attack by Banju, his arch-enemy. 
Bingu decided to encrypt all the strings he had, by the following method. Every substring of identical letters is replaced by a single instance of that letter 
followed by the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it.

Example 1:
Input:
s = "aabc"
Output: 1c1b2a
Explanation: aabc
Step1: a2b1c1
Step2: 1c1b2a

Example 2:
Input:
s = "aaaaa"
Output: 5a
Explanation: aaaaa
Step 1: a5
Step 2: 5a

Your Task: You don't need to read input or print anything.Your task is to complete the function encryptString() which takes a single argument(s) and returns 
the encrypted string.

Expected Time Complexity: O(|s|).
Expected Auxiliary Space: O(|s|).
*/

// Link --> https://practice.geeksforgeeks.org/problems/encrypt-the-string-10337/1/#

// Code:
class Solution
{
public:
    string encryptString(string s)
    {
        int counter = 0;
        string ans;
        
        for(int i=0 ; i<s.size() ; i++)
        {
            counter++;
            if((i+1 < s.size()) && (s[i] == s[i+1]))
                continue;
                
            ans += s[i];
            ans += to_string(counter);
            counter = 0;
        }
        reverse(ans.begin(), ans.end());
	    return ans;
    }
};
