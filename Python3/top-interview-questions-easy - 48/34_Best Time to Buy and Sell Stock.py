# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        min_value, max_invest = prices[0], 0
        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            if (prices[i] - min_value) > max_invest:
                max_invest = prices[i] - min_value
        return max_invest