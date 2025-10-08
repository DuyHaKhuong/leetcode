"""
LeetCode: Coin Change
URL: https://leetcode.com/problems/coin-change/
Difficulty: Medium
Fetched: 2025-10-05 06:41:21

Description:
You are given an integer array coins representing coin denominations and an integer
amount representing a total amount of money. Return the fewest number of coins
needed to make up that amount. If it is not possible to make the amount using any
combination of the coins, return -1. You may assume an infinite number of each coin.

Examples:
- Example 1
  Input: coins = [1, 2, 5], amount = 11
  Output: 3
  Explanation: 11 = 5 + 5 + 1.

- Example 2
  Input: coins = [2], amount = 3
  Output: -1
  Explanation: No combination makes 3 using only 2.

- Example 3
  Input: coins = [1], amount = 0
  Output: 0
  Explanation: Zero coins are needed to make amount 0.

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        print(coins)
        dp = {coin: 1 for coin in coins}

        def _find_min(value, limit=float('inf')):
            if value in dp:
                return dp[value]
            if limit == 0:
                return float('inf')
            min_coins = float('inf')
            for coin in coins:
                if coin > value:
                    continue
                result = _find_min(value - coin, limit=min_coins - 1)
                if result != -1:
                    min_coins = min(min_coins, result + 1)
            dp[value] = min_coins
            return min_coins
        result = _find_min(amount)

        return result if result != float('inf') else -1

if __name__ == "__main__":
    sol = Solution()
    coins = [1, 2, 5]
    print(sol.coinChange(coins, 50))
    # self.assertEqual(sol.coinChange([1, 2, 5], 11), 3)
    # self.assertEqual(sol.coinChange([2], 3), -1)
    # self.assertEqual(sol.coinChange([1], 0), 0)
