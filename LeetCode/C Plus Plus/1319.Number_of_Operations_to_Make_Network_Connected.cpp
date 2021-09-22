/*
Problem Statement:
-----------------
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between 
computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected 
computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 

Example 1:
---------
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:
---------
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:
---------
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

Example 4:
---------
Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0
*/

// Link --> https://leetcode.com/problems/number-of-operations-to-make-network-connected/

// Code:
class Solution 
{
public:
    void dfs(int source, vector<int> graph[], vector<int> &visited)
    {
        visited[source] = 1;
        for(auto v : graph[source])
        {
            if(!visited[v])
                dfs(v, graph, visited);
        }
    }
    
    int makeConnected(int n, vector<vector<int>>& connections) 
    {
        // Counting the number of edges and creating a graph for further DFS
        vector<int> graph[n];
        int edges = connections.size();
        int components = 0;
        
        for(int i=0; i<edges; i++)
        {
            graph[connections[i][0]].push_back(connections[i][1]);
            graph[connections[i][1]].push_back(connections[i][0]);
        }
        
        if(edges < n-1)    // we cannot connect all vertices.
            return -1;
        
        // If both the base cases fails, then we have (components - 1) edges extra.
        else
        {            
            vector<int> visited(n, 0);
            for(int i=0; i<n; i++)
            {
                if(!visited[i])
                {
                    dfs(i, graph, visited);
                    components++;
                }
            }
        } 
        
        return (components-1);
    }
};

