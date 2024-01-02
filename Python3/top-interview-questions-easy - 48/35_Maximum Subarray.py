# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        sum_value, max_value = nums[0], nums[0]
        for i in range(1,len(nums)):
            sum_value = max(sum_value + nums[i], nums[i])
            max_value = max(max_value, sum_value)
        return max_value