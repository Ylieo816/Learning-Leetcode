# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        # String
        value = 0
        mini = prices[0]
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] - mini > value:
                value = prices[i] - mini
        return value 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP
        dp = [0] * len(prices)
        mini = prices[0]
        for i in range(len(prices)):
            dp[i] = max(dp[i-1], prices[i] - mini)
            mini = min(mini, prices[i])
        return dp[-1]
        
        
        
        