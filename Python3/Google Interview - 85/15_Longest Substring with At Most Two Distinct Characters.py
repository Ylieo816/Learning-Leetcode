# Given a string s, return the length of the longest substring that contains at most two distinct characters.

# Sliding Window
# Complexity
# Time complexity: O(n)
# Space complexity: O(1)
# same soluion as "Fruit Into Baskets"
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        left = 0
        table = defaultdict(int)
        max_val = 2
        for right in range(len(s)):
            table[s[right]] += 1

            if len(table) > 2:
                table[s[left]] -= 1
            
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1
        return right - left + 1