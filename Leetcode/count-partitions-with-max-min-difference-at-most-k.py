"""
You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.
"""

from typing import List
from collections import deque
from sortedcontainers import SortedList 

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        print(nums)
        n = len(nums)
        MOD = 10 ** 9 + 7
        if n == 1:
            return 1 

        # dp[i][j] is the number of partitions of nums[i:] with max - min <= j 
        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n - 1] = 1 
        
        # Use sorted list to keep track all elements 
        # Find min, max efficiently
        sl = SortedList([nums[n-1]])
        max_idx = n - 1
        c_total = 2
        for i in range(n - 2, -1, -1):
            # Consider adding nums[i]
            num = nums[i]
            sl.add(num)
            while (sl[-1] - sl[0]) > k:
                sl.remove(nums[max_idx])
                c_total -= dp[max_idx + 1]
                max_idx -= 1 
            print("num = ", num, "max index", max_idx, nums[max_idx])
            dp[i] = c_total 
            c_total = (c_total + dp[i]) % MOD
        print(dp)
        return dp[0]
            

    def countPartitionsV1(self, nums: List[int], k: int) -> int:
        # Let dp[i] is the number of partitions of nums[i:] 
        n = len(nums)
        MOD = 10 ** 9 + 7
        if n == 1:
            return 1 

        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n - 1] = 1 
        # Calculate dp[i] 
        min_val, max_val = nums[n-1], nums[n-1]
        for i in range(n - 2, -1, -1):
            if min_val <= nums[i] <= max_val:
                dp[i] = (2 * dp[i + 1]) % MOD
                continue 

            # A set of partitions with nums[i] only, add dp[i + 1] 
            dp[i] = dp[i + 1]
            min_val, max_val = nums[i], nums[i]
            for j in range(i + 2, n + 1):
                new_min_val = min(min_val, nums[j - 1])
                new_max_val = max(max_val, nums[j - 1])
                if new_max_val - new_min_val <= k:
                    dp[i] = (dp[i] + dp[j]) % MOD
                    min_val, max_val = new_min_val, new_max_val
                else:
                    break
        print(dp)
        return dp[0]


# Input: nums = [9,4,1,3,7], k = 4
# print(Solution().countPartitions(nums = [9,4,1,3,7], k = 4))
# Input: [21,3,21], k = 13 
print(Solution().countPartitions(nums = [21,3,21], k = 13))
