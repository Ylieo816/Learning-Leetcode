# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1