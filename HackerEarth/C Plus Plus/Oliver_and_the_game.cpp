/*
Problem Statement:
-----------------
Oliver and Bob are best friends. They have spent their entire childhood in the beautiful city of Byteland. The people of Byteland live happily along with the King.
The city has a unique architecture with total N houses. The King's Mansion is a very big and beautiful bungalow having address = 1. Rest of the houses in Byteland 
have some unique address, (say A), are connected by roads and there is always a unique path between any two houses in the city. Note that the King's Mansion is also 
included in these houses.

Oliver and Bob have decided to play Hide and Seek taking the entire city as their arena. In the given scenario of the game, it's Oliver's turn to hide and Bob is 
supposed to find him. Oliver can hide in any of the houses in the city including the King's Mansion. As Bob is a very lazy person, for finding Oliver, 
he either goes towards the King's Mansion (he stops when he reaches there), or he moves away from the Mansion in any possible path till the last house on that path.

Oliver runs and hides in some house (say X) and Bob is starting the game from his house (say Y). If Bob reaches house X, then he surely finds Oliver.

Given Q queries, you need to tell Bob if it is possible for him to find Oliver or not.

The queries can be of the following two types:
0 X Y : Bob moves towards the King's Mansion.
1 X Y : Bob moves away from the King's Mansion

INPUT :
The first line of the input contains a single integer N, total number of houses in the city. Next N-1 lines contain two space separated integers A and B denoting a 
road between the houses at address A and B.
Next line contains a single integer Q denoting the number of queries.
Following Q lines contain three space separated integers representing each query as explained above.

OUTPUT :
Print "YES" or "NO" for each query depending on the answer to that query.
*/

// Link --> https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/oliver-and-the-game-3/

// Code:
#include <bits/stdc++.h>
using namespace std;
#define int long long int

vector <int> inTime;
vector <int> outTime;
int timer = 0;

void resize(int n)
{
	inTime.resize(n + 1);
	outTime.resize(n + 1);
}

void dfs(int source, int parent, vector<int> graph[])
{
	inTime[source] = timer++;

	for(auto i: graph[source])
	{
		if(i != parent)
			dfs(i, source, graph);
	}
	outTime[source] = timer++;
}

bool check(int x, int y)
{
	if(inTime[x] > inTime[y] and outTime[x] < outTime[y])
		return true;

	return false;
}

int32_t main()
{
	int n;
	cin >> n;

	timer = 1;
	resize(n);

	vector<int> graph[n+1];
	for(int i=0; i<n-1; i++)
	{
		int x, y;
		cin >> x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}
	int source = 1;
	int parent = 0;
	dfs(source, parent, graph);

	int q;
	cin>>q;

	for(int i=0; i<q; i++)
	{
		int type, x, y;
		cin >> type >> x >> y;

		if(!check(x, y) and !check(y, x))
		{
			cout << "NO" << endl;
			continue;
		}

		if(type == 0)
		{
			if(check(y, x))
				cout << "YES" << endl;
			else
				cout << "NO" << endl;
		}

		else if(type == 1)
		{
			if(check(x, y))
				cout << "YES" << endl;
			else
				cout << "NO" << endl;
		}
	}

	return 0;
}
