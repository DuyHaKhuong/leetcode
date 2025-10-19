"""
Title: Climbing Stairs II
URL: https://leetcode.com/problems/climbing-stairs-ii/
Difficulty: Medium
Fetched: 2025-10-17 14:04:48

You are climbing a staircase with n + 1 steps, numbered from 0 to n.

You are also given a 1-indexed integer array costs of length n, where costs[i]
is the cost of step i.

From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost of
jumping from step i to step j is defined as: costs[j] + (j - i)^2.

You start from step 0 with cost = 0. Return the minimum total cost to reach
step n.

Examples:
- Input: n = 4, costs = [1, 2, 3, 4]
  Output: 13
  Explanation: One optimal path is 0 → 1 → 2 → 4 with costs:
  0→1: costs[1] + (1 - 0)^2 = 1 + 1 = 2
  1→2: costs[2] + (2 - 1)^2 = 2 + 1 = 3
  2→4: costs[4] + (4 - 2)^2 = 4 + 4 = 8
  Total = 2 + 3 + 8 = 13.

- Input: n = 4, costs = [5, 1, 6, 2]
  Output: 11
  Explanation: One optimal path is 0 → 2 → 4 with costs:
  0→2: costs[2] + (2 - 0)^2 = 1 + 4 = 5
  2→4: costs[4] + (4 - 2)^2 = 2 + 4 = 6
  Total = 5 + 6 = 11.

- Input: n = 3, costs = [9, 8, 3]
  Output: 12
  Explanation: Optimal path is 0 → 3 with total cost costs[3] + (3 - 0)^2 = 3 + 9 = 12.

Constraints:
- 1 <= n == costs.length <= 10^5
- 1 <= costs[i] <= 10^4
"""

from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # """
        # Returns the minimum total cost to reach step n.
        # """
        min_costs = {0: 0, -1: float('inf'), -2: float('inf')}
        for j in range(1, n + 1):
            min_cost = float('inf')
            for step in [1, 2, 3]:
                cost = min_costs[j - step] + costs[j - 1] + step * step
                min_cost = min(min_cost, cost)
            min_costs[j] = min_cost
        # print([min_costs[i] for i in range(n + 1)])
        return min_costs[n]

        back1 = back2 = back3 = 0                                   # <-- 1)

        for stepCost in costs:                                      # <-- 2)
            minCost = min(back1 + 1, back2 + 4, back3 + 9)


            back1, back2, back3  = stepCost+minCost, back1, back2   # <-- 3)

        return back1                                                # <-- 4)

    def check_examples(self) -> None:
        # Example 1
        print(self.climbStairs(4, [1, 2, 3, 4]))  # Expected: 13
        # Example 2
        print(self.climbStairs(4, [5, 1, 6, 2]))  # Expected: 11
        # Example 3
        print(self.climbStairs(3, [9, 8, 3]))     # Expected: 12


if __name__ == "__main__":
    sol = Solution()
    # Run example calls (uncomment to execute):
    sol.check_examples()
    # Or run a single custom call:
    # print(sol.climbStairs(4, [1, 2, 3, 4]))
