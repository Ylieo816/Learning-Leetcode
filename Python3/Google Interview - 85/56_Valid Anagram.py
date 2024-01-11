# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # string doesn't support "s.sort()", need use sorted but speed low
        return sorted(s) == sorted(t)

# Complexity Analysis
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        return Counter(s) == Counter(t)