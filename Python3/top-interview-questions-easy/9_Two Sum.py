# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, v in enumerate(nums):
            if (target - v) in table:
                return [table[target - v], i]
            table[v] = i
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            if (target - nums[i]) in table:
                return [i, table[target - nums[i]]]
            table[nums[i]] = i
