/*
Problem Statement:
-----------------
In a candy store, there are N different types of candies available and the prices of all the N different types of candies are provided to you.
You are now provided with an attractive offer.
You can buy a single candy from the store and get at most K other candies ( all are different types ) for free.
Now you have to answer two questions. Firstly, you have to find what is the minimum amount of money you have to spend to buy all the N different candies. 
Secondly, you have to find what is the maximum amount of money you have to spend to buy all the N different candies.
In both the cases you must utilize the offer i.e. you buy one candy and get K other candies for free.

Example 1:
---------
Input:
N = 4
K = 2
candies[] = {3 2 1 4}
Output:
3 7

Explanation: As according to the offer if you buy one candy you can take at most two more for free. So in the first case, you buy the candy which costs 1 and 
takes candies worth 3 and 4 for free, also you buy candy worth 2 as well. So min cost : 1+2 =3. In the second case, you can buy the candy which costs 4 and takes candies 
worth 1 and 2 for free, also you need to buy candy worth 3 as well. So max cost : 3+4 =7.

Example 2:
----------
Input: 
N = 5
K = 4
candies[] = {3 2 1 4 5}
Output: 
1 5

Explanation: For minimimum cost buy the candy with the cost 1 and get all the other candies for free. For maximum cost buy the candy with
the cost 5 and get all other candies for free.

Your Task: You don't need to read input or print anything. Your task is to complete the function candyStore() which takes the array candies[], its size N 
and an integer K as input parameters and returns the minimum amount and maximum amount of money to buy all candies according to the offer.

Expected Time Complexity: O(NLogN)
Expected Auxiliary Space: O(1)
*/

// Link --> https://practice.geeksforgeeks.org/problems/shop-in-candy-store1145/1

// Code:
class Solution
{
public:
    int utilCandy(int a[] , int n , int k)
    {
        int total = 0;
        int i = 0;
        
        while(i <= n)
        {
            total += a[i];
            i++;
            n -= k;
        }
        return total;
    }
    
    vector<int> candyStore(int candies[], int n, int k)
    {
        vector<int> result;
        
        sort(candies , candies+n);
        result.push_back(utilCandy(candies , n-1 , k));
        
        reverse(candies , candies+n);
        result.push_back(utilCandy(candies , n-1 , k));
        
        return result;
    }
};
