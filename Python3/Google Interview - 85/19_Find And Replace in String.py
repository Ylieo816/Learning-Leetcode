# You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

# To complete the ith replacement operation:

# Check if the substring sources[i] occurs at index indices[i] in the original string s.
# If it does not occur, do nothing.
# Otherwise if it does occur, replace that substring with targets[i].
# For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

# All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

# For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
# Return the resulting string after performing all replacement operations on s.

# A substring is a contiguous sequence of characters in a string.

# Time complexity: O(n+kM), n is list answer by s, join is O(n)
# Space complexity: O(m+n), n is length of s, m is the total length of all target words
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        answer = list(s)
        for idx, src, tgt in zip(indices, sources, targets):
            lengthOfSrc = len(src)
            if s[idx: idx + lengthOfSrc] == src:
                answer[idx] = tgt
                # answer[idx+1:idx+lengthOfSrc] = ''
                for i in range(idx+1, idx+lengthOfSrc):
                    answer[i] = ""
        return ''.join(answer)

# few test can't pass
# # Time Complexity: O(M+N)
# # Space Complexity: O(M+N): M for dict and N for answer
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        list_all = {}
        for i in range(len(indices)):
            list_all[indices[i]] = (sources[i], targets[i])

        idx = 0
        answer = ''
        while idx < len(s):
            if idx in list_all and s[idx:].startswith(list_all[idx][0]):
                answer += list_all[idx][1]
                idx += len(list_all[idx][0])
            else:
                answer += s[idx]
                idx += 1
        return answer