/*
Problem Statement:
-----------------
Given a BST and a key K. If K is not present in the BST, Insert a new Node with a value equal to K into the BST. 
Note: If K is already present in the BST, don't modify the BST.

Example 1:
---------
Input:
     2
   /   \
  1     3
K = 4
Output: 1 2 3 4
Explanation: After inserting the node 4, Inorder traversal will be 1 2 3 4.

Example 2:
---------
Input:
        2
      /   \
     1     3
             \
              6
K = 4
Output: 1 2 3 4 6
Explanation: After inserting the node 4, Inorder traversal of the above tree will be 1 2 3 4 6.

Your Task: You don't need to read input or print anything. Your task is to complete the function insert() which takes the root of the BST and
Key K as input parameters and returns the root of the modified BST after inserting K. 
Note: The generated output contains the inorder traversal of the modified tree.

Expected Time Complexity: O(Height of the BST).
Expected Auxiliary Space: O(1).
*/

// Link --> https://practice.geeksforgeeks.org/problems/insert-a-node-in-a-bst/1#

// Code:
Node* insert(Node* root, int key)
{
    if(key < root->data && root->left != NULL)
        root = insert(root->left , key);
    
    else if(key < root->data && root->left == NULL)
    {
        Node *newnode = new Node(key);
        root->left = newnode;
        return root->left;
    }
    
    else if(key > root->data && root->right != NULL)
        root = insert(root->right , key);
    
    else if(key > root->data && root->right == NULL)
    {
        Node *newnode = new Node(key);
        root->right = newnode;
        return root->right;
    }
    
    return root;
}
