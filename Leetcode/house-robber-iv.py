"""
LeetCode: House Robber IV
URL: https://leetcode.com/problems/house-robber-iv/
Difficulty: Medium
Fetched: 2025-10-05 22:15:29

Description:
There are several consecutive houses on a street, each with some amount of money.
A robber refuses to steal from adjacent houses. The capability of the robber is the
maximum amount stolen from any single house among the houses he robs.

You are given an integer array nums where nums[i] is the money in the i-th house,
and an integer k, the minimum number of houses the robber will steal from. It is
always possible to steal at least k houses. Return the minimum capability achievable
over all ways to rob at least k non-adjacent houses.

Examples:
- Example 1
  Input: nums = [2, 3, 5, 9], k = 2
  Output: 5
  Explanation: Rob indices (0, 2) -> max(2, 5) = 5; other valid pairs yield 9.
  Minimum capability among options is 5.

- Example 2
  Input: nums = [2, 7, 9, 3, 1], k = 2
  Output: 2
  Explanation: Rob indices (0, 4) -> max(2, 1) = 2, which is minimal.

Constraints:
- 1 <= nums.length <= 1e5
- 1 <= nums[i] <= 1e9
- 1 <= k <= (nums.length + 1) / 2

Thinking: nums = [n0, n1, n2, ..., n_m], k
min(picked numbers)

nums[:m], k =>
  nums[:m - 1], k
  max((nums[:m - 2], k - 1), n_m)
"""

from typing import *
from functools import lru_cache

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = 1, max(nums)

        def _check(cap: int) -> bool:
            count = 0
            i = 0
            while i < len(nums) and count < k:
                if nums[i] <= cap:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        while right - left >= 1:
            # left <= mid < right
            mid = (left + right) // 2
            if _check(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def minCapabilityV2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        # Solve for k = 1
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = min(dp[i - 1], nums[i])
        for j in range(2, k + 1):
            new_dp = [0] * n
            new_dp[0] = new_dp[1] = float('inf')

            for i in range(2, n):
                new_dp[i] = min(
                    new_dp[i - 1],
                    max(dp[i - 2], nums[i])
                )
            dp = new_dp
        return dp[-1]


    def minCapabilityv1(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        # Solve j = 1
        dp[0][1] = nums[0]
        for i in range(1, n):
                dp[i][1] = min(dp[i - 1][1], nums[i])

        # Solve i = 0
        for j in range(2, k + 1):
            dp[0][j] = float('inf')
        # solve i = 1
        dp[1][1] = min(nums[0], nums[1])
        for j in range(2, k + 1):
            dp[1][j] = float('inf')


        @lru_cache(None)
        def _get_min_capability(i, j) -> int:
            if j == 1 or i <= 1:
                return dp[i][j]

            # include nums[i]
            min_cap1 = max(
                nums[i],
                _get_min_capability(i - 2, j - 1),
            )
            # exclude nums[i]
            min_cap2 = _get_min_capability(i - 1, j)
            min_cap = min(min_cap1, min_cap2)
            dp[i][j] = min_cap
            return min_cap

        val = _get_min_capability(n - 1, k)
        return val

if __name__ == "__main__":
    # Code to run examples (not tests)
    sol = Solution()
    # print(sol.minCapability([2, 3, 5, 9], 2))     # Expected: 5
    print(sol.minCapability([4,22,11,14,25], 3))
    # print(sol.minCapability([2, 7, 9, 3, 1], 2))  # Expected: 2
