/*
Problem Statement:
-----------------
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
---------
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
---------
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:
-----------
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
*/

// Link --> https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

// Code:
class Solution 
{
public:
    int maxLevelSum(TreeNode* root) 
    {
        queue <TreeNode*> q;
        queue <int> qLevel;
        int maxLevel = 0, maxSum = INT_MIN;
        int lastLevel = 1, lastSum = 0;
        TreeNode* node;
        
        q.push(root);
        qLevel.push(lastLevel);
        
        while(!q.empty())
        {
            node = q.front();
          
            q.pop();
            
            lastLevel = qLevel.front();
            qLevel.pop();
            
            lastSum += node->val;
            
            if(node->left)
            {
                q.push(node->left);
                qLevel.push(lastLevel+1);
            }
            
            if(node->right)
            {
                q.push(node->right);
                qLevel.push(lastLevel+1);
            }
            
            if(lastLevel != qLevel.front())
            {
                if(lastSum > maxSum)
                {
                    maxSum = lastSum;
                    maxLevel = lastLevel;
                }
                lastSum = 0;
            }
        }
        
        return maxLevel;
    }
};
