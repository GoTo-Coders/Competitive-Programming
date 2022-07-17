"""
Problem Statement:
------------------
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons). Note that 1 does not map to any letters.

Example 1:
----------
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
----------
Input: digits = ""
Output: []

Example 3:
----------
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
  - 0 <= digits.length <= 4
  - digits[i] is a digit in the range ['2', '9'].

"""

# Link --> https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Code:
class Solution:
    def helper(self, s, letters, index, output, answer):
        # handling the base case.
        if index >= len(s):
            answer.append("".join(output))
            return

        # getting the first pressed number
        number = int(s[index])

        # extracting the string present on the current number
        numberValue = letters[number]

        for i in range(len(numberValue)):
            # adding the current character
            output.append(numberValue[i])

            # recursively calling the helper function
            self.helper(s, letters, index+1, output, answer)

            # backtracking
            output.pop()
        
    def letterCombinations(self, s: str) -> List[str]:
        answer = []
        letters = ["", "", "abc", "def", "ghi",
               "jkl", "mno", "pqrs", "tuv", "wxyz"]

        if len(s) == 0:
            return answer

        output = []
        index = 0

        self.helper(s, letters, index, output, answer)
        return answer
