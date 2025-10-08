"""
LeetCode: Maximum Number of Subsequences After One Inserting
URL: https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/
Difficulty: Medium
Fetched: 2025-09-27 15:03:20

Description:
Given an uppercase string s, you may insert at most one uppercase letter at any
position (including start or end). Return the maximum number of "LCT" subsequences
obtainable after at most one insertion.

Examples:
- Input: s = "LMCT"  -> Output: 2
  Explanation: Insert 'L' at the start to get "LLMCT"; subsequences at [0,3,4] and [1,3,4].
- Input: s = "LCCT"  -> Output: 4
  Explanation: Insert 'L' at the start to get "LLCCT"; subsequences at [0,2,4], [0,3,4], [1,2,4], [1,3,4].
- Input: s = "L"     -> Output: 0
  Explanation: Cannot form "LCT" with a single insertion.

Constraints:
- 1 <= s.length <= 1e5
- s consists of uppercase English letters.

Thinking:
LLL CCCC.. TTT..
Insert:
L: #C x #T (begin)
T: #L x #C (end)
C: #L x #T (somewhere in middle)
=> For each C, compute the # combinations, requires #L forward, #T backward = (total Ts - #T forward)
=> insert 1: add the max(*combinations, insert L at begin, insert C at the end)
"""

from typing import *


class Solution:
    def numOfSubsequences(self, s: str) -> int:
        """Return the maximum number of 'LCT' subsequences after at most one insertion."""
        # list of tuple np.array([#L, #C, #T])
        num_t = s.count('T')
        num_l, num_c = 0, 0
        n_combinations = 0
        max_combination = 0
        n_ct_combine = 0
        n_lc_combine = 0
        for l in s:
            if l == 'T':
                num_t -= 1
            elif l == 'L':
                num_l += 1
            elif l == 'C':
                num_c += 1
                n_combination = num_l * num_t
                n_combinations += n_combination
                n_lc_combine += num_l
                n_ct_combine += num_t
            else:
                continue
            max_combination = max(max_combination, num_l * num_t)
        # Compute max_combination if inserting L or T 
        max_combination = max(max_combination, n_ct_combine, n_lc_combine)
        return n_combinations + max_combination


sol = Solution()
# print(sol.numOfSubsequences("LMCT"))
# print(sol.numOfSubsequences("LCCT"))
# print(sol.numOfSubsequences("L"))
# print(sol.numOfSubsequences("LT"))
# print(sol.numOfSubsequences("LCTLCLT"))


# if __name__ == "__main__":
#     import unittest

#     class Tests(unittest.TestCase):
#         def setUp(self):
#             self.sol = Solution()

#         def test_example_1(self):
#             # s = "LMCT" -> insert 'L' at start => 2 subsequences of "LCT"
            # self.assertEqual(self.sol.numOfSubsequences("LMCT"), 2)

        # def test_example_2(self):
        #     # s = "LCCT" -> insert 'L' at start => 4 subsequences
        #     self.assertEqual(self.sol.numOfSubsequences("LCCT"), 4)

        # def test_example_3(self):
        #     # s = "L" -> cannot obtain "LCT" with one insertion
        #     self.assertEqual(self.sol.numOfSubsequences("L"), 0)

    # unittest.main(verbosity=2)
