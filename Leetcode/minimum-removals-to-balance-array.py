"""
Title: Minimum Removals to Balance Array
URL: https://leetcode.com/problems/minimum-removals-to-balance-array/
Difficulty: Medium
Fetched: 2025-09-28 19:09:43

Description:
You are given an integer array nums and an integer k. An array is considered
balanced if its maximum element is at most k times its minimum element.
You may remove any number of elements from nums, but the array must remain
non-empty. Return the minimum number of elements to remove so that the
remaining array is balanced.

Examples:
- Input: nums = [2, 1, 5], k = 2
  Output: 1
  Explanation: Remove 5 -> [2, 1]; now 2 <= 1 * 2.

- Input: nums = [1, 6, 2, 9], k = 3
  Output: 2
  Explanation: Remove 1 and 9 -> [6, 2]; 6 <= 2 * 3.

- Input: nums = [4, 6], k = 2
  Output: 0
  Explanation: Already balanced since 6 <= 4 * 2.

Constraints:
- 1 <= nums.length <= 1e5
- 1 <= nums[i] <= 1e9
- 1 <= k <= 1e5

Thinking:
nums: sorted n0, n1, n2..n_k
for n_i, find n_j: n_j <= n_i * k => (i, j) is valid
Find maximum (j - i + 1), answer = len(nums) - max(j - i + 1)
"""

from typing import *


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        low, high = 0, 0
        max_balance_length = 1
        for low, num in enumerate(nums):
            while nums[high] <= num * k and high < N:
                high += 1
            max_balance_length = max(max_balance_length, high - low)
            if high == N:
                break
        return N - max_balance_length


if __name__ == "__main__":
    import unittest

    class Tests(unittest.TestCase):
        def test_examples(self):
            sol = Solution()
            # Example 1
            self.assertEqual(sol.minRemoval([2, 1, 5], 2), 1)
            # Example 2
            self.assertEqual(sol.minRemoval([1, 6, 2, 9], 3), 2)
            # # Example 3
            self.assertEqual(sol.minRemoval([4, 6], 2), 0)

    # Uncomment to run tests locally
    unittest.main(verbosity=2)
