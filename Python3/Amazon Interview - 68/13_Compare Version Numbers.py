# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

version1 = "1.01"
version2 = "1.001"

# Split + Parse, Two Pass
# Time complexity : O(N+M+max⁡(N,M)), where N and M are lengths of input strings.
# Space complexity : O(N+M) to store arrays v1 and v2.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        lv1, lv2 = len(v1), len(v2)

        for i in range(max(lv1, lv2)):
            i1 = int(v1[i]) if i < lv1 else 0
            i2 = int(v2[i]) if i < lv2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0