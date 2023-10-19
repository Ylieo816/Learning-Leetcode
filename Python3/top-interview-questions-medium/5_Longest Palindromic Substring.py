# Given a string s, return the longest palindromic substring in s.

# Best answer
# Time Complex - O(n * n) where n is the length of the input string
# Space Complex - O(1) 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ''
        for i in range(len(s)):
            par_twoSame = self.get_internal_pal(s, i, i+1)
            par = self.get_internal_pal(s, i, i)
            pal = max([pal, par_twoSame, par], key=len)
        return pal

    def get_internal_pal(self, s, l, r):
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

# # DP table to record each ce
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]  # use dp[i][j] to represent s[i:j]
        pal = s[0]
        for i in range(len(s)):
            dp[i][i] = True # only one char, it is still a pal
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i+1, len(s)):    # only check upper area from the diagonal since oreder is i to j
                if s[i] == s[j]: # check if two char are same no matter it is neibor of the pal two sides
                    if (j - i) == 1 or dp[i+1][j-1] == True:
                        # j - i = 1 ==> neibor are same
                        # dp[i+1][j-1] ==> if sub_string > 2, check the inner string is also pal
                        dp[i][j] = True
                        if len(pal) < len(s[i:j+1]):
                            # if new sub_string is longer than ori max
                            pal = s[i:j+1]
        return pal

