"""
Problem Statement:
------------------
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
  push(x) – Push element x onto stack.
  pop() – Removes the element on top of the stack.
  top() – Get the top element.
  getMin() – Retrieve the minimum element in the stack.
  
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :
Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1
NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor.
"""
 
# Link --> https://www.interviewbit.com/problems/min-stack/
 
# Code: 
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, x):
        self.stack.append(x)
        
        if self.min_stack:
            self.min_stack.append(min(x, self.min_stack[-1]))
        else:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        else:
            pass

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:   
            return -1

    # @return an integer
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:   
            return -1 
          
          
