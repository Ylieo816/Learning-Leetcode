# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_table, t_table = {}, {}
        for s1, t1 in zip(s, t):
            if (s1 in s_table and s_table[s1] != t1) or (t1 in t_table and t_table[t1] != s1):
                return False
            s_table[s1] = t1
            t_table[t1] = s1
        return True

# Time Complexity : O(N)
# Space Complexity: O(N)
class Solution(object):
    def isIsomorphic(self, s, t):
        s_table, t_table = [], []
        for idx in s:
            s_table.append(s.index(idx))
        for idx in t:
            t_table.append(t.index(idx))
        if s_table == t_table:
            return True
        return False