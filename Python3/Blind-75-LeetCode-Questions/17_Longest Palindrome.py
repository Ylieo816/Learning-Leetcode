# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1: return 1
        table = Counter(s)
        one_flag = 0
        count = 0
        for c in table:
            count += (table[c] // 2)
            if table[c] % 2 == 1:
                one_flag = 1
        return 2 * count + 1 * one_flag