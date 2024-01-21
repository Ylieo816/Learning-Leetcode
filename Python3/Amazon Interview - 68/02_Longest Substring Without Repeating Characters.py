# Given a string s, find the length of the longest substring without repeating characters.

# Sliding Window with Dict
# Time complex: O(n)
# Space complexity : O(min(m,n))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        record = {}
        max_val = 0
        for right in range(len(s)):
            if s[right] not in record or record[s[right]] < left:
                max_val = max(max_val, right - left + 1)
            else:
                left = record[s[right]] + 1
            record[s[right]] = right

        return max_val
    
#  set with add/remove between start and end
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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