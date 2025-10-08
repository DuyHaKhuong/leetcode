"""
LeetCode: Minimum Time to Activate String
URL: https://leetcode.com/problems/minimum-time-to-activate-string/
Difficulty: Medium
Fetched: 2025-10-04 15:44:18

Description:
You are given a string s of length n and an integer array order, where order is a
permutation of the indices [0, n - 1]. Starting at time t = 0, and at each integer
time t, replace the character at index order[t] in s with '*'.

A substring is valid if it contains at least one '*'. The string is active if the
total number of valid substrings is greater than or equal to k. Return the minimum
time t at which s becomes active. If it never becomes active after all replacements,
return -1.

Examples:
- Example 1
  Input: s = "abc", order = [1, 0, 2], k = 2
  Output: 0
  Explanation: At t = 0, s becomes "a*c". Valid substrings containing '*' are
  "*", "a*", "*c", and "a*c" (4 in total). Since 4 >= 2, the answer is 0.

- Example 2
  Input: s = "cat", order = [0, 2, 1], k = 6
  Output: 2
  Explanation: t = 0 -> "*at" (3 valid); t = 1 -> "*a*" (5 valid);
  t = 2 -> "***" (all 6 substrings are valid). Minimum t is 2.

- Example 3
  Input: s = "xy", order = [0, 1], k = 4
  Output: -1
  Explanation: Even after all replacements, the number of valid substrings is 3 < 4.

Constraints:
- 1 <= n == s.length <= 1e5
- order.length == n
- order is a permutation of [0, n - 1]
- 0 <= order[i] <= n - 1
- s consists only of lowercase English letters
- 1 <= k <= 1e9
"""

from typing import *
from sortedcontainers import SortedList


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        indices = SortedList([-1, len(s)])
        n_active = 0
        # Incrementally update sorted list
        for t, idx in enumerate(order):
            position = indices.bisect_left(idx)
            n_active += (idx - indices[position - 1]) * (indices[position] - idx)
            # print(indices, position, left_count, right_count, n_active)
            indices.add(idx)
            if n_active >= k:
                return t
        return -1


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_examples(self):
            sol = Solution()
            self.assertEqual(sol.minTime("abc", [1, 0, 2], 2), 0)
            self.assertEqual(sol.minTime("cat", [0, 2, 1], 6), 2)
            self.assertEqual(sol.minTime("xy", [0, 1], 4), -1)

    unittest.main()
