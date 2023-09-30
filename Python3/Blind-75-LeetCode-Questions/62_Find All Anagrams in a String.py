# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Complexity:
# - Time: O(n) one pass over the p, on pass for s, and for every letter in s we iterate over values in hashmap (maximum 26)
# - Space: O(1) hashmap with max 26 keys
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer, s_l, p_l = [], len(s), len(p)
        
        if p_l > s_l:   
            return answer
        char_freqs = Counter(p)
        
        # initial first window
        for i in range(p_l - 1):
            if s[i] in char_freqs:
                char_freqs[s[i]] -= 1
        
        for i in range(-1, s_l - p_l + 1):
            # the char move out of window, add back
            if i > -1 and s[i] in char_freqs:
                char_freqs[s[i]] += 1
            # the char in window, sub it
            if (i + p_l) < s_l and s[i + p_l] in char_freqs:
                char_freqs[s[i + p_l]] -= 1

            # if table is empty: answer it
            if all(v == 0 for v in char_freqs.values()):
                answer.append(i+1)
        
        return answer