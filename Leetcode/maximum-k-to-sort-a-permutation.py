"""
LeetCode: Maximum K to Sort a Permutation
URL: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
Difficulty: Medium
Fetched: 2025-10-04 23:44:15

Description:
You are given an integer array nums of length n, where nums is a permutation of
the integers in the range [0, n - 1]. You may swap elements at indices i and j
only if (nums[i] & nums[j]) == k, where & is the bitwise AND operation and k is a
non-negative integer.

Return the maximum value of k such that the array can be sorted in non-decreasing
order using any number of allowed swaps. If nums is already sorted, return 0.

Examples:
- Example 1
  Input: nums = [0, 3, 2, 1]
  Output: 1
  Explanation: Choose k = 1. Swapping nums[1] = 3 and nums[3] = 1 is allowed since
  (3 & 1) == 1, resulting in [0, 1, 2, 3].

- Example 2
  Input: nums = [0, 1, 3, 2]
  Output: 2
  Explanation: Choose k = 2. Swapping nums[2] = 3 and nums[3] = 2 is allowed since
  (3 & 2) == 2, resulting in [0, 1, 2, 3].

- Example 3
  Input: nums = [3, 2, 1, 0]
  Output: 0
  Explanation: Only k = 0 allows the necessary swaps; no larger k works.

Constraints:
- 1 <= n == nums.length <= 1e5
- 0 <= nums[i] <= n - 1
- nums is a permutation of [0, n - 1]


Thinking: nums[i] & nums[j] == k means that all bits in k must be set in both nums[i] and nums[j].
i < j, nums[i] > nums[j] -> need swap either
   nums[i], nums[h]

nums[i] != i -> need to swap
  nums[idx] == k
"""

from typing import *

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        value = None
        for i, num in enumerate(nums):
            if num == i:
                continue
            if value is None:
                value = num
            else:
                value = value & num
        return value

if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_examples(self):
            sol = Solution()
            # Example 1
            self.assertEqual(sol.sortPermutation([0, 3, 2, 1]), 1)
            # Example 2
            self.assertEqual(sol.sortPermutation([0, 1, 3, 2]), 2)
            # Example 3
            self.assertEqual(sol.sortPermutation([3, 2, 1, 0]), 0)

    unittest.main()
