"""
Title: Distinct Points Reachable After Substring Removal
URL: https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/
Difficulty: Medium
Fetched: 2025-10-17 13:05:16

You are given a string s consisting of characters 'U', 'D', 'L', and 'R',
representing moves on an infinite 2D Cartesian grid:
- 'U': (x, y) -> (x, y + 1)
- 'D': (x, y) -> (x, y - 1)
- 'L': (x, y) -> (x - 1, y)
- 'R': (x, y) -> (x + 1, y)

You are also given a positive integer k. You must choose and remove exactly one
contiguous substring of length k from s. Then, starting from (0, 0), perform
the remaining moves in order.

Return the number of distinct final coordinates reachable.

Examples:
- Input: s = "LUL", k = 1
  Output: 2
  Explanation: After removing a length-1 substring, s can be "UL", "LL", or
  "LU", which end at (-1, 1), (-2, 0), and (-1, 1) respectively. The distinct
  final points are (-1, 1) and (-2, 0).

- Input: s = "UDLR", k = 4
  Output: 1
  Explanation: Removing all 4 characters yields the empty string, which ends at
  (0, 0). Only one distinct point.

- Input: s = "UU", k = 1
  Output: 1
  Explanation: After removing a length-1 substring, s becomes "U", which always
  ends at (0, 1).

Constraints:
- 1 <= s.length <= 10^5
- s consists only of 'U', 'D', 'L', and 'R'
- 1 <= k <= s.length
"""
import numpy as np

class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        """
        Returns the number of distinct final coordinates reachable after
        removing exactly one substring of length k and executing remaining moves.
        """
        steps = {
            'U': complex(0, 1),
            'D': complex(0, -1),
            'L': complex(-1, 0),
            'R': complex(1, 0),
        }
        combine_steps = {
            b: {a: steps[b] - steps[a] for a in steps}
            for b in steps
        }
        n = len(s)
        step_k = complex(0, 0)
        a = np.array([combine_steps[s[i]][s[i+k]] for i in range(n-k)], dtype=complex)
        prefix = np.unique(np.cumsum(a))
        if step_k in prefix:
            return len(prefix)
        else:
            return len(prefix) + 1


    def check_examples(self) -> None:
        # Example 1
        print(self.distinctPoints("LUL", 1))   # Expected: 2
        # Example 2
        print(self.distinctPoints("UDLR", 4))  # Expected: 1
        # Example 3
        print(self.distinctPoints("UU", 1))    # Expected: 1


if __name__ == "__main__":
    sol = Solution()
    # Run example calls (uncomment to execute):
    sol.check_examples()
    # Or run a single custom call:
    # print(sol.distinctPoints("LUL", 1))
