# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

# Return the reformatted license key.

# Optimized
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = (s.upper()).replace("-","")[::-1]
        answer = ''
        for i in range(0, len(s), k):
            answer += s[i:i+k] + "-"
        return answer[::-1][1:]

# Loop with if else
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        answer = ''
        cnt = k
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '-':
                continue

            if cnt > 0:
                cnt -= 1
            else:
                answer += '-'
                cnt = k - 1
            
            answer += s[i].upper()
        return answer[::-1]