# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        list to all values
        if len(nums) == 0: return 0
        elif len(nums) < 2: return max(nums[0], nums[-1])
        
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#         return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        # best dp
        pre = now = 0
        for v in nums:
            pre, now = now, max(now, pre + v)
        return now