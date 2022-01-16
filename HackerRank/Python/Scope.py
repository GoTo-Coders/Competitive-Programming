# Link --> https://www.hackerrank.com/challenges/30-scope/problem

# Code:
def computeDifference(self):
        maxDiff = 0
        elements = self.__elements
        
        for i in range(len(elements)):
            for j in range(i+1 , len(elements)):
                current_diff = abs(elements[j] - elements[i])
                if current_diff > maxDiff:
                    maxDiff = current_diff
                
        self.maximumDifference = maxDiff
