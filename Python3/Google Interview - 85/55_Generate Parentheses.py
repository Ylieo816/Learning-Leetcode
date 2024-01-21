# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Backtracking
# Complexity Analysis
# Time complexity: O(4^n/(n^(1/2)))
# Space complexity: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        # two integer variables left & right to see how many '(' & ')' are in the current string
        # If left < n then we can add '(' to the current string
        # If right < left then we can add ')' to the current string
        def backtrack(combination, left, right):
            if len(combination) == n * 2:
                answer.append(combination)
                return
            
            if left < n:
                backtrack(combination + '(', left + 1, right)
            if right < left:
                backtrack(combination + ')', left, right + 1)

        backtrack('', 0, 0)
        return answer