/*
Problem Statement:
-----------------
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node 
{
    public int val;
    public List<Node> neighbors;
}
 
Test case format:
-----------------
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
---------
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
---------
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:
----------
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Example 4:
---------
Input: adjList = [[2],[1]]
Output: [[2],[1]]
*/

// Link --> https://leetcode.com/problems/clone-graph/

// Code:
/*
// Definition for a Node.
class Node 
{
public:
    int val;
    vector<Node*> neighbors;
    Node() 
    {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) 
    {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) 
    {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution 
{
public:
    void dfs(Node *answer, Node *node, vector<Node*> &visited)
    {
        // Marking the current vertex as visited.
        visited[answer->val] = answer;
        
        for(auto v : node->neighbors)
        {
            // v is basically the current vertex.
            if(visited[v->val] == NULL)
            {
                Node *newNode = new Node(v->val);
                // Adding current vertex to the answer vertex.
                (answer->neighbors).push_back(newNode);
                dfs(newNode, v, visited);
            }
            // Undirected graph, so connect current vertex to the answer.
            else   
            {
                (answer->neighbors).push_back(visited[v->val]);
            }
        }
    }
    
    Node* cloneGraph(Node* node) 
    {
        if (node == NULL)
            return NULL;
        
        vector<Node*> visited(1000, NULL);
        
        Node *answer = new Node(node->val);
        dfs(answer, node, visited);
        
        return answer;
    }
};


