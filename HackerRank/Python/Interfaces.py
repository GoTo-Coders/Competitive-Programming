# Link --> https://www.hackerrank.com/challenges/30-interfaces/problem

# Code:
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
                
        return sum(divisors)
