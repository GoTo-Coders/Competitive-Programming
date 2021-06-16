/*
Problem Statement:
-----------------
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.
3. Follow up: Can you solve it with time complexity O(height of tree)?

Example 1:
---------
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7].
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
---------
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
---------
Input: root = [], key = 0
Output: []

Constraints:
-----------
The number of nodes in the tree is in the range [0, 104].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5
*/

// Link --> https://leetcode.com/problems/delete-node-in-a-bst/

// Code:
/*
 * Definition for a binary tree node.
 * struct TreeNode 
 {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x),                left(left), right(right) {}
 };
*/

class Solution 
{
public:
    
    TreeNode* switchNode(TreeNode* root)
    {
        while(root->left != NULL && root != NULL)
            root = root->left;
        
        return root;
    }
    
    TreeNode* deleteNode(TreeNode* root, int key) 
    {
        if(root == NULL)
            return NULL;
        
        else
        {
            if(root->val > key)
                root->left = deleteNode(root->left , key);
            
            else if(root->val < key)
                root->right = deleteNode(root->right , key);
            
            else                //root->val == key
            {
                if(root->left == NULL)
                {
                    TreeNode *temp = root->right;
                    delete root;
                    return temp;
                }
                
                else if(root->right == NULL)
                {
                    TreeNode *temp = root->left;
                    delete root;
                    return temp;
                }
                
                TreeNode *temp = switchNode(root->right);
                root->val = temp->val;
                root->right = deleteNode(root->right , temp->val);
            }
        }
        return root;
    }
};
