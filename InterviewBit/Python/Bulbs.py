"""
Problem Description
-------------------
N light bulbs are connected by a wire.
Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.
Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Problem Constraints
0 <= N <= 5e5
0 <= A[i] <= 1

Input Format
The first and the only argument contains an integer array A, of size N.

Output Format
Return an integer representing the minimum number of switches required.

Example Input
A = [0 1 0 1]

Example Output
4

Example Explanation
press switch 0 : [1 0 1 0]
press switch 1 : [1 1 0 1]
press switch 2 : [1 1 1 0]
press switch 3 : [1 1 1 1
"""

# Link --> https://www.interviewbit.com/problems/interview-questions/

# Code:
class Solution:
    """
    # Time Complexity: O(N ^ 2)
    def bulbs(self, a):
        count = 0
        for i in range(len(a)):
            if a[i] == 0:
                count += 1
                for j in range(i, len(a)):
                    a[j] = not a[j]
                
        return count
    """
    
    # Time Complexity: O(N)
	def bulbs(self, a):
        count = 0
        
        for bit in a:
            """
            if the count is even that means we have flipped the bulbs 
            even number of times hence the bit remained same.
            Else, we have flip the bit.
            """
            if count % 2 == 0:
                bit = bit
            else:
                bit = not bit
            # incrementing the count or cost
            if bit % 2 == 1:
                continue
            else:
                count += 1
                
        return count
      
      
