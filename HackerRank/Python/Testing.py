# Link --> https://www.hackerrank.com/challenges/30-testing/problem

# Code:
class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        return list()

class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        return [7,9,1,2,-7,10,22]

    @staticmethod
    def get_expected_result():
        return 4

class TestDataExactlyTwoDifferentMinimums(object):
    @staticmethod
    def get_array():
        return [7,9,1,2,-7,10,22,-7]

    @staticmethod
    def get_expected_result():
        return 4
