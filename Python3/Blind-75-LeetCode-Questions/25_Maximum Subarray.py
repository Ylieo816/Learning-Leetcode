# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Clean Code
        if len(nums) == 0: return 0
        
        sum_value, max_value = nums[0], nums[0]
        for i in range(1,len(nums)):
            # use to find all subarray by shifting window
            sum_value = max(sum_value + nums[i], nums[i])
            # use to find the max subarray
            max_value = max(max_value, sum_value)
        return max_value

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #  Faster code
        sum_val = max_val = nums[0]
        for i in range(1, len(nums)):
            sum_val = nums[i] + (sum_val if sum_val > 0 else 0)
            if sum_val > max_val: max_val = sum_val        
        return max_val