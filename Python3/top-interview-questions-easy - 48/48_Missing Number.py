# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Math mothod
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        total = (1 + l) * l / 2
        return int(total - sum(nums))

# Find one number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i