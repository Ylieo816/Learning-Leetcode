# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Time Complexity: O(nW), where n is the number of elements in nums and W is sum(nums)
# Space Complexity: O(W/2)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        dp = [True] + [False] * (total // 2)
        for num in nums:
            for current in range(total // 2, num-1, -1):
                # - current sum has been seen before, don't select the current element, the sum will not change.
                # - current sum has not been seen before, but it can be obtained by selecting the current element.
                # dp[curr-num] = True
                # - current sum has not been seen before, and it cannot be obtained by selecting the current element. Total sum will still not exist, and its dp value remains False.
                dp[current] = dp[current] or dp[current - num]

        return dp[-1]
    

# Optimization, replace the dp array with a set(), don't need to store False for a value that has not yet been obtained.

