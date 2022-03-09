# Link --> https://practice.geeksforgeeks.org/problems/anagram-1587115620/1

# Code:
class Solution:
    def isAnagram(self,a,b):
        return sorted(a) == sorted(b)
