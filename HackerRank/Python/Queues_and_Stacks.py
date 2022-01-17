# Link --> https://www.hackerrank.com/challenges/30-queues-stacks/problem

# Code:
class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self, ch):
        return self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        return self.queue.append(ch)
    
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        return self.queue.pop(0)
