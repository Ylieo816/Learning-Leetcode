# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# DP
# Complexity
# - Time complexity: ( O(n * m) ), where ( n ) is the length of the string and ( m ) is the maximum length of a word in the dictionary.
# - Space complexity: ( O(n) )
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0]= True

        # map is used to calcul data to func
        # max_len use to reduce unnecessary iterations
        max_len = max(map(len, wordDict)) 
        for i in range(1, len(s)+1):
            for j in range(i-1, max(i - max_len - 1, -1), -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

# Tre to check with startswith()
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def construct(current, wordDict, memo = {}):
            if current in memo:
                return memo[current]

            if not current:
                return True

            for word in wordDict:
                if current.startswith(word):
                    new_cur = current[len(word):]
                    if construct(new_cur, wordDict, memo):
                        memo[current] = True
                        return True
            memo[current] = False
            return False

        return construct(s, wordDict)