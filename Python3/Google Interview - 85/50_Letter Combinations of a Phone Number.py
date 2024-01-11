# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Backtracking Algorithm
# - Time complexity: ( O(4^n) ), where ( n ) is the length of the input string. In the worst case, each digit can represent 4 letters, so there will be 4 recursive calls for each digit.
# - Space complexity: ( O(n) ), where ( n ) is the length of the input string. This accounts for the recursion stack space.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if not digits:
            return answer
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                answer.append(combination)
            else:
                for s in phone[next_digits[0]]:
                    backtrack(combination + s, next_digits[1:])
        
        backtrack('', digits)
        return answer

# Iteration
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = ['']
        for digit in digits:
            new_combinations = []
            for combination in combinations:
                for c in phone[digit]:
                    new_combinations.append(combination + c)
            combinations = new_combinations
        return combinations