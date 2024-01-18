# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Two pointer
# Time complexity : O(N)
# Space complexity : O(1)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        table = {
            '0':'0', '1':'1', '6':'9', '8':'8', '9':'6'
        }

        left, right = 0, len(num) - 1

        while left <= right:
            if (num[left] not in table) or (table[num[left]] != num[right]):
                return False
            left += 1
            right -= 1
        return True