# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        a = ord('A')
        for c in (columnTitle):
            answer = 26 * answer + (ord(c) - a) + 1
        return answer