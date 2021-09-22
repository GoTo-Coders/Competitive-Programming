/*
Problem Statement:
-----------------
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, 
or 0 if no such sequence exists.

Example 1:
---------
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
--------
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
*/

// Link -> https://leetcode.com/problems/word-ladder/

// Code:
class Solution 
{
public:
    int ladderLength(string start , string end, vector<string>& wordlist) 
    {
        int wordSize = start.size();
        int length = 0;             // contain the actual length required.
        queue<string> q;
        q.push(start);
        
        // To retrieve words in O(1) time, using a set.
        unordered_set<string> word;
        
        // Inserting all the words in the set.
        for(int i=0; i<wordlist.size(); i++)
            word.insert(wordlist[i]);
        
        // Check if the end word is not present in the list.
        if(word.find(end) == word.end())
            return 0;
        
        while(!q.empty())
        {
            length++;
            int qlen = q.size();
            // iterating for each word of the current queue.
            // hence using queue-length.
            for(int i=0; i<qlen; i++)
            {
                string s = q.front();
                q.pop();
                
                // iterating through each character of the current string i.e. 's'
                for(int j=0; j<wordSize; j++)
                {
                    char org = s[j];
                    for(char ch = 'a'; ch<='z'; ch++)
                    {
                        s[j] = ch;
                        if(s == end)
                            return length+1;
                        if(word.find(s) == word.end())
                            continue;
                        word.erase(s);
                        q.push(s);
                    }
                    s[j] = org;
                }
            }
        }
        return 0;
    }
};
