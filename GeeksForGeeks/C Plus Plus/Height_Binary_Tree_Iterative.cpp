/*
Given a binary tree, find its height.


Example 1:

Input:
     1
    /  \
   2    3
Output: 2
Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   

Your Task:
You don't need to read input or print anything. Your task is to complete the function height() which takes root node of the tree as input parameter and returns an integer denoting the height of the tree. If the tree is empty, return 0. 


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105

*/


// Method to iteratively find the height of the tree.
int BinaryTree::Height(BinaryTree *root){

    // If tree contains no node.
    if(root == NULL)
        return 0;

    // Create a queue to insert the nodes of each level in it
    queue<BinaryTree*> queue;

    // Initially insert the root of the tree.
    queue.push(root);

    // and initialize height with 0
    int height = 0;

    while(1){

        // nodeCount is the number of nodes at any level of tree
        // which is equal to the size of the queue at that instant.
        int nodeCount = queue.size();

        // If queue is empty, then  we have reached the end of the tree.
        if(nodeCount == 0)
            return height;
        
        height++;

        // Otherwise, remove the element from 
        while(nodeCount>0){

            BinaryTree *node = queue.front();
            queue.pop();

            if(node->left != NULL)
                queue.push(node->left);

            if(node->right != NULL)
                queue.push(root->right);

            nodeCount--;
        }
    }
}
