# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i, val in enumerate(s):
            if count[val] == 1:
                return i
        return -1