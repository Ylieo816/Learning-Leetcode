# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  set with add/remove between start and end
        max_val = 0
        chara = set()
        start = 0
        for end in range(len(s)):
            if s[end] not in chara:
                chara.add(s[end])
                max_val = max(max_val, end - start + 1)
            else:
                while (s[end] in chara):
                    chara.remove(s[start])
                    start += 1
                chara.add(s[end])
        return max_val

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  dict
        dic = {}
        start = 0
        max_val = 0
        for end in range(len(s)):
            if s[end] not in dic or dic[s[end]] < start:
                dic[s[end]] = end
                max_val = max(max_val, end - start + 1)
            else:
                start = dic[s[end]] + 1
                dic[s[end]] = end
        return max_val