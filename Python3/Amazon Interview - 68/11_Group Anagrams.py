# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Time Complexity: O(NKlog⁡K), N is the length of strs, K is the maximum length of a string in strs, sort each string in O(Klog⁡K) time
# Space Complexity: O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            s_sort = ''.join(sorted(s))
            dic[s_sort].append(s)

        return dic.values()