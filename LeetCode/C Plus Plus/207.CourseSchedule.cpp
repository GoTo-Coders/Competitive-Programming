/*
Problem Statement:
-----------------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
---------
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

Example 2:
---------
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. 
So it is impossible.
*/

// Link -> https://leetcode.com/problems/course-schedule/

// Code:
class Solution 
{
public:
     bool DFS(vector<int>& visited, unordered_map<int, vector<int>>& graph, int i)
     {
        if(visited[i] == 11) 
            return false;
         
        if (visited[i] == 1)
            return true;
         
        visited[i]=11; 
        for(auto c: graph[i])
        {
            if(!DFS(visited, graph, c))
                return false;
        }
         
        visited[i] = 1;     
        return true;
    }
    
    bool canFinish(int courses, vector<vector<int>>& tasks) 
    {
        unordered_map<int, vector<int>> graph;
        vector<int> visited(courses, 0);
        
        for(auto p: tasks)
        {
            graph[p[0]].push_back(p[1]);
        }
        
        for(int i=0; i<courses; i++)
        {
            if (!DFS(visited, graph, i))
                return false;
        }
        
        return true;
    }
};
