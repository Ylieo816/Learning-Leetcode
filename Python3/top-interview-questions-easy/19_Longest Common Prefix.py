# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(min(strs))
        for i in range(m):
            s = strs[0][i]
            for j in range(1, len(strs)):
                if s != strs[j][i]:
                    return strs[0][:i]
        return min(strs)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        word_long = min(strs, key=len)

        for i, char in enumerate(word_long):
            for word in strs:
                if word[i] != char:
                    return word_long[:i]
        return word_long