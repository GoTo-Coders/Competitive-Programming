/*
Problem Statement:
-----------------
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
 
Example 1:
---------
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
---------
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
*/

// Link --> https://leetcode.com/problems/merge-intervals/

// Code:
class Solution 
{
public:
    vector <vector<int>> merge(vector <vector<int>>& v) 
    {
        vector<vector<int>> result;
        
        // Sorting the 2-D vector.
        sort(begin(v) , end(v));
        
        for(const auto &interval : v) 
        {
            // interval[0] is basically first element of v[i].
            
            if (empty(result) || interval[0] > result.back()[1]) 
                result.emplace_back(interval);
            
            else 
                result.back()[1] = max(result.back()[1], interval[1]);
        }
        return result;
    }
};
