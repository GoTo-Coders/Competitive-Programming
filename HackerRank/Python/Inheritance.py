# Link --> https://www.hackerrank.com/challenges/30-inheritance/problem

# Code:
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        # Calling parent class's constructor:
        super().__init__(firstName, lastName, idNumber)
        
        # Initializing child class variables:
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        
    
    def calculate(self):
        from statistics import mean
        
        average = int(mean(scores))
        if average < 40:
            return 'T'
        elif average < 55:
            return 'D'
        elif average < 70:
            return 'P'
        elif average < 80:
            return 'A'
        elif average < 90:
            return 'E'
        else:
            return 'O'
