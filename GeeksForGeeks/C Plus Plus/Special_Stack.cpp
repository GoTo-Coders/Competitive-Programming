/*
Problem Statement:
------------------
Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() 
which should return minimum element from the SpecialStack. Your task is to complete all the functions, using stack data-Structure.

Example 1:
---------
Input:
Stack: 18 19 29 15 16
Output: 15
Explanation: The minimum element of the stack is 15.

Your Task: Since this is a function problem, you don't need to take inputs. You just have to complete 5 functions, push() which takes the stack and an integer x as 
input and pushes it into the stack; pop() which takes the stack as input and pops out the topmost element from the stack; isEmpty() which takes the stack as input 
and returns true/false depending upon whether the stack is empty or not; isFull() which takes the stack and the size of the stack as input and returns true/false 
depending upon whether the stack is full or not (depending upon the given size); getMin() which takes the stack as input and returns the minimum element of the stack. 
Note: The output of the code will be the value returned by getMin() function.

Expected Time Complexity: O(N) for getMin, O(1) for remaining all 4 functions.
Expected Auxiliary Space: O(1) for all the 5 functions.
*/

// Link --> https://practice.geeksforgeeks.org/problems/special-stack/1

// Code:
void push(stack<int>& s, int a)
{
	s.push(a);
}

bool isFull(stack<int>& s,int n)
{
	if(s.size() == n)
	    return true;
	return false;
}

bool isEmpty(stack<int>& s)
{
	if(s.empty())
	    return true;
	return false;
}

int pop(stack<int>& s)
{
	int top = s.top();
	s.pop();
	return top;
}

int getMin(stack<int>& s)
{
	stack <int> temp;
	temp = s;
	int min = 99999;
	
	while(!temp.empty())
	{
	    if(temp.top() < min)
	        min = temp.top();
	        
	    temp.pop();
	}

    return min;
}
