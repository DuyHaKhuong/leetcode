"""
LeetCode: Maximum Total from Optimal Activation Order
URL: https://leetcode.com/problems/maximum-total-from-optimal-activation-order/
Difficulty: Medium
Fetched: 2025-10-05 06:29:12

Description:
You are given two integer arrays `value` and `limit`, both of length `n`. All elements
start inactive, and you may activate them in any order.

To activate an inactive element at index `i`, the current number of active elements
must be strictly less than `limit[i]`. When you activate `i`, add `value[i]` to the
running total. After each activation, if the number of active elements becomes `x`,
then all indices `j` with `limit[j] <= x` become permanently inactive (even if already active).

Return the maximum total achievable by choosing the activation order optimally.

Examples:
- Example 1:
  Input: value = [3, 5, 8], limit = [2, 1, 3]
  Output: 16
  Explanation: One optimal order is i = 1 (total 5), then i = 0 (total 8), then i = 2 (total 16).

- Example 2:
  Input: value = [4, 2, 6], limit = [1, 1, 1]
  Output: 6
  Explanation: Activate i = 2 (value 6); all items with limit <= 1 become inactive. Total is 6.

- Example 3:
  Input: value = [4, 1, 5, 2], limit = [3, 3, 2, 3]
  Output: 12
  Explanation: An optimal activation order yields total 12 after four activations.

Constraints:
- 1 <= n == value.length == limit.length <= 1e5
- 1 <= value[i] <= 1e5
- 1 <= limit[i] <= n
"""

from typing import *


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        pass


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_examples(self):
            sol = Solution()
            # Example 1
            self.assertEqual(sol.maxTotal([3, 5, 8], [2, 1, 3]), 16)
            # Example 2
            self.assertEqual(sol.maxTotal([4, 2, 6], [1, 1, 1]), 6)
            # Example 3
            self.assertEqual(sol.maxTotal([4, 1, 5, 2], [3, 3, 2, 3]), 12)

    unittest.main()
