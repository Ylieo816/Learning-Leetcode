# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Time complexity : O(S*n), On each step the algorithm finds the next F(i) in n iterations, where 1≤i≤S
# Space complexity : O(S)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP to calculate each num need Coin
        minCoin = [amount + 1] * (amount + 1)
        minCoin[0] = 0

        for curNum in range(amount+1):
            for coin in coins:
                if coin <= curNum:
                    # minCoins[curNum]: number of coins needed to make amount curNum
                    # minCoins[curNum-coin]: number of coins needed to make the amount before adding 
                    #                   the current coin to it (+1 to add the current coin)
                    minCoin[curNum] = min(minCoin[curNum], minCoin[curNum - coin] + 1)
        
        if minCoin[amount] == (amount + 1):
            return -1

        return minCoin[amount]