# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.


# Sliding window across s, tracking the char
# O(s + t) time: O(t) to build t_counter, then O(s) to move our sliding window across s. Each index is only visited twice.
# O(s + t) space: O(t) space for t_counter and O(s) space for s_counter
# make a sliding window across s, tracking the char
# O(s + t) time: O(t) to build t_counter, then O(s) to move our sliding window across s. Each index is only visited twice.
# O(s + t) space: O(t) space for t_counter and O(s) space for s_counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        missing = len(t)
        need = collections.defaultdict(int)

        for char in t:
            need[char] += 1

        answer = [-1, -1]
        left = 0
        for right in range(len(s)):
            # extend the right side of window
            need[s[right]] -= 1
            if need[s[right]] >= 0:
                missing -= 1

            # after containing all need char, shorten the left side of window
            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                # compare if smaller than origin
                if answer[1] == -1 or (right - left < answer[1] - answer[0]):
                    answer = [left, right]

        return '' if answer == [-1, -1] else s[answer[0] : answer[1] + 1]

# slower but easy
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_l, t_l = len(s), len(t)
        if not s or not t or s_l < t_l:
            return ''
        
        t_count = Counter(t)
        # chars_len = len(t_count.keys())
        chars_len = len(set(t))

        s_count = Counter()
        window_size = 0
        answer = ''

        start, end = 0, -1

        while(start < s_l):
            # window_size window if window smaller than need
            if window_size < chars_len:
                # reach end, return answer or empty
                if end == s_l - 1:
                    return answer
                end += 1

                s_count[s[end]] += 1
                if t_count[s[end]] > 0 and s_count[s[end]] == t_count[s[end]]:
                    window_size += 1
                
            # Shorten window
            else:
                s_count[s[start]] -= 1
                if t_count[s[start]] > 0 and s_count[s[start]] == t_count[s[start]] - 1:
                    window_size -= 1
                start += 1

            
            # updete answer:
            if window_size == chars_len:
                if not answer or (end - start + 1) < len(answer):
                    answer = s[start : end+1]

        return answer

