# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Array - One pass
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_val = prices[0], 0
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            if (prices[i] - min_val) > max_val:
                max_val = prices[i] - min_val
        return max_val

# DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        min_val = prices[0]
        for i in range(len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_val)
            min_val = min(min_val, prices[i])
        return dp[-1]