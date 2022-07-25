"""
Problem Statement:
------------------
Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop element from queue and print the poped element)

Example 1:
---------
Input:
Q = 5
Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation:
In the first test case for query 
1 2   the queue will be {2}
1 3   the queue will be {2 3}
2     poped element will be 2 the queue will be {3}
1 4   the queue will be {3 4}
2     poped element will be 3 

Example 2:
---------
Input:
Q = 4
Queries = 1 3 2 2 1 4   
Output: 3 -1
Explanation:
In the second testcase for query 
1 3   the queue will be {3}
2     poped element will be 3 the queue will be empty
2     there is no element in the queue and hence -1
1 4   the queue will be {4}. 

Your Task : You are required to complete the two methods push() which take one argument an integer 'x' to be pushed into the queue and pop() 
which returns a integer poped out from othe queue. If the queue is empty, it should return -1 on a pop operation. 

Expected Time Complexity: O(1) for both push() and pop().
Expected Auxiliary Space: O(1) for both push() and pop().
"""

# Link --> https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1

# Code:
class MyQueue:
    def __init__(self):
        self.arr=[]
        
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if len(self.arr) > 0:
            element = self.arr[0]
            self.arr.remove(element)
            return element
        return -1
      
      


