/*
    Given N cities, some of them have roads in between them. Geek is in city 1. The task is to find the minimum number of roads needed to construct so that geek can visit any city from any other city.

    Note:
    1. All the cities are numbered from 1 to N.
    2. No two cities have multiple roads.
    3. No city has self road

    Input:
    1. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
    2. The first line of each test case contains two space_separated integers N and M.
    3. Next M lines contain two space-separated integers u and v, represents a road between cities u and v

    Output: For each test case, print the answer

    Constraints:
    1. 1 <= T <= 100
    2. 1 <= N <= 50
    3. 0 <= M <= min(1000, N*(N-1)/2)

    Example:
    Input:
    2
    4 2
    1 2
    3 4
    5 5
    1 2
    2 3
    3 4
    4 5
    5 1

    Output:
    1
    0
*/

/*
    Link to the question : https://practice.geeksforgeeks.org/problems/geek-and-city/0/
*/

// Solution

#include <bits/stdc++.h>
using namespace std;

void DFS(int v, vector<bool> &visited, vector<int>adj[])
{
    visited[v] = true;
    
    for(auto i = adj[v].begin(); i != adj[v].end(); i++)
    {
        if( !visited[*i] )
        {
            DFS(*i, visited, adj);
        }
    }
}

int findNoOfRoads(int N, vector<int> adj[])
{
    vector<bool> visited(N, false);
    int count = -1;
    
    for(int i = 0; i < N; i++)
    {
        if(!visited[i])
        {
            DFS(i, visited, adj);
            count++;
        }
    }
    return count;
}

int main() {
	int t;
	cin>>t;
	
	while(t--)
	{
	    int N, M;
	    cin>>N>>M;
	    vector<int> adj[N];
	    while(M--)
	    {
	        int u, v;
	        cin>>u>>v;
	        
	        adj[u-1].push_back(v-1); 
	        adj[v-1].push_back(u-1);
	    }
	    
	    int ans = findNoOfRoads(N, adj);
	    cout<<ans<<endl;
	}
	return 0;
}