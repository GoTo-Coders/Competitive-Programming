/*
Problem Statement:
-----------------
The member states of the UN are planning to send 2 people to the moon. They want them to be from different countries. 
You will be given a list of pairs of astronaut ID's. Each pair is made of astronauts from the same country. 
Determine how many pairs of astronauts from different countries they can choose from.
*/

// Link --> https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=false

// Code:
#include <bits/stdc++.h>
#define int         long long int

using namespace std;


void dfs(int u, vector<int> &visited, vector<int> graph[] , int &count)
{
    visited[u] = 1;
    count++;
    
    for(auto x: graph[u])
    {
        if(!visited[x])
            dfs(x, visited, graph, count);
    }
}

int32_t main()
{
    int v,e;
    cin >> v >> e;
    
    // Initializing graph with the input, this will make people 
    // of same country as a connected component.
    vector<int> graph[v];
    for(int i=0; i<e; i++)
    {
        int x,y;
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    
    vector<int> solution;
    vector<int> visited(v, 0);
    
    for(int i=0; i<v; i++)
    {
        if(!visited[i])
        {
            // Count will count vertices in a component.
            int count = 0;
            dfs(i, visited, graph, count);
            // stroing the count of vertices of each component.
            solution.push_back(count);
        }   
    }
    
    // Initially answer will contain total pairs formed by vertices.
    // It will use the (n C 2) formula to ci=ount pairs.
    int answer = (v *(v - 1)) / 2 ;
    
    // Now, counting the pairs formed by vertices with the
    // vertices of their compnents.
    for(int i=0; i<solution.size(); i++)
    {
        int self_pair = (solution[i] * (solution[i] - 1)) / 2;
        answer = answer - self_pair;
    }
    
    // Finally subtracting (total - self_pairs) to get answer.
    cout << answer;
}
