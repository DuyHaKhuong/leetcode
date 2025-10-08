"""
LeetCode: Remove K-Balanced Substrings
URL: https://leetcode.com/problems/remove-k-balanced-substrings/
Difficulty: Medium
Fetched: 2025-10-07 06:55:42

Description:
You are given a string s consisting only of '(' and ')', and an integer k. A string
is k-balanced if it is exactly k consecutive '(' followed by k consecutive ')',
that is, '(' * k + ')' * k (for example, when k = 3 the k-balanced string is
"((()))").

Repeatedly remove all non-overlapping k-balanced substrings from s and join the
remaining parts, until no k-balanced substring exists. Return the final string
after all possible removals.

Examples:
- Example 1
  Input: s = "(())", k = 1
  Output: ""
  Explanation: Remove "()" twice: (()) -> () -> "".

- Example 2
  Input: s = "(()(", k = 1
  Output: "(("
  Explanation: Only one "()" can be removed: "(()(" -> "((".

- Example 3
  Input: s = "((()))()()()", k = 3
  Output: "()()()"
  Explanation: Remove "((()))" once; the rest stays as "()()()".

Constraints:
- 2 <= s.length <= 1e5
- s consists only of '(' and ')'
- 1 <= k <= s.length / 2
"""

from typing import *


class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        # ( -> 0, ) -> 1
        stack = []
        open_count = 0
        close_count = 0
        for ch in s:
            if ch == '(':
                close_count = 0
                open_count += 1
                stack.append((ch, open_count))
            else:
                open_count = 0
                close_count += 1
                stack.append((ch, close_count))
                if close_count != k:
                    continue

                # consider pruning here
                if len(stack) < 2 * k or stack[-k - 1][1] < k:
                    continue
                for _ in range(2*k):
                    stack.pop()
                if len(stack) > 0:
                    _ch, count = stack[-1]
                    if _ch == '(':
                        open_count, close_count = count, 0
                    else:
                        open_count, close_count = 0, count

        return ''.join(ch for ch, _ in stack)


if __name__ == "__main__":
    # Code to run examples (not tests)
    sol = Solution()
    # print(sol.removeKBalancedSubstrings("(())", 1))          # Expected: ""
    # print(sol.removeKBalancedSubstrings("(()(", 1))          # Expected: "(("
    # print(sol.removeKBalancedSubstrings("((()))()()()", 3))  # Expected: "()()()"
    s = "(()(()(()))((()"
    k = 2
    print(sol.removeSubstring(s, k))  # Expected: "(()((()"
