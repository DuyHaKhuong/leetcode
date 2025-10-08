"""
LeetCode: House Robber II
URL: https://leetcode.com/problems/house-robber-ii/
Difficulty: Medium
Fetched: 2025-10-05 21:01:25

Description:
You are a professional robber planning to rob houses arranged in a circle. Each house
has some amount of money. Because the houses form a circle, the first and last houses
are adjacent. If two adjacent houses are robbed on the same night, the police are
alerted.

Given an integer array nums where nums[i] is the amount of money at the i-th house,
return the maximum amount you can rob without alerting the police.

Examples:
- Example 1
  Input: nums = [2, 3, 2]
  Output: 3
  Explanation: You cannot rob houses 1 and 3 since they are adjacent in the circle.

- Example 2
  Input: nums = [1, 2, 3, 1]
  Output: 4
  Explanation: Rob houses 1 and 3 for a total of 4.

- Example 3
  Input: nums = [1, 2, 3]
  Output: 3
  Explanation: Rob house 3 (3) or house 2 (2); maximum is 3.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000


Thinking:
n0, n1,....n_k

n_{k + 1}: f(k + 1)
- f(k)
- n_{k + 1} + g(k - 1)
 g: n1, n2, ..., n_{k-1}
 g(k) = g(k - 1) or g(k - 2) + n_k
"""

from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        a1 = nums[1]
        a2 = max(nums[1], nums[2])

        b1 = max(nums[0], nums[1])
        b2 = max(nums[0] + nums[2], nums[1])

        for i in range(3, n - 1):
            a3 = max(a2, nums[i] + a1)
            a1, a2 = a2, a3
            b3 = max(b2, nums[i] + b1)
            b1, b2 = b2, b3
        return max(nums[-1] + a1, b2)


if __name__ == "__main__":
    # Code to run examples (not tests)
    sol = Solution()
    # print(sol.rob([2, 3, 2]))      # Expected: 3
    # print(sol.rob([1, 2, 3, 1]))   # Expected: 4
    print(sol.rob([1,1,1,1]))
    # print(sol.rob([1, 2, 3]))      # Expected: 3
