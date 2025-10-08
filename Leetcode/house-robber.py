"""
LeetCode: House Robber
URL: https://leetcode.com/problems/house-robber/
Difficulty: Medium
Fetched: 2025-10-05 20:50:34

Description:
You are a professional robber planning to rob houses along a street. Each house has
some amount of money. However, adjacent houses have connected security systems and
the police are contacted if two adjacent houses are robbed on the same night.

Given an integer array nums representing the amount of money at each house, return
the maximum amount of money you can rob without alerting the police.

Examples:
- Example 1
  Input: nums = [1, 2, 3, 1]
  Output: 4
  Explanation: Rob house 1 (1) and house 3 (3), total = 4.

- Example 2
  Input: nums = [2, 7, 9, 3, 1]
  Output: 12
  Explanation: Rob houses 1 (2), 3 (9), and 5 (1), total = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""

from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return sum(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, n):
            nums[i] = max(
                nums[i - 1],
                nums[i] + nums[i - 2]
            )
        return nums[-1]

if __name__ == "__main__":
    # Examples from the description (not tests)
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))  # Expected: 4
    print(sol.rob([2, 7, 9, 3, 1]))  # Expected: 12
