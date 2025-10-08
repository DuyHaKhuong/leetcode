"""
3592. Inverse Coin Change
Medium
Topics
premium lock icon
Companies
Hint
You are given a 1-indexed integer array numWays, where numWays[i] represents the number of ways to select a total amount i using an infinite supply of some fixed coin denominations. Each denomination is a positive integer with value at most numWays.length.

However, the exact coin denominations have been lost. Your task is to recover the set of denominations that could have resulted in the given numWays array.

Return a sorted array containing unique integers which represents this set of denominations.

If no such set exists, return an empty array.
"""

from typing import List 

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        # Find numWays[i] for i = 1, 2, ..
        coins = []
        ways = [0] * n
        # ways[0] = 1
        print(numWays)
        for i in range(n):
            coin = i + 1
            if numWays[i] == ways[i]:
                continue # coin i + 1 does not exist
            elif numWays[i] != ways[i] + 1:
                # No set of denomination satisfies this array.
                return []
            coins.append(coin)
            ways[i] += 1
            for j in range(i + 1, n):
                ways[j] += ways[j - coin]
            print(i + 1, ways)
        return coins 

numWays = [0,1,0,2,0,3,0,4,0,5]
numWays = [1,2,2,3,4]
numWays = [1,2,3,4,15]
print(Solution().findCoins(numWays))