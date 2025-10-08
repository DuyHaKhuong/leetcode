"""
3603. Minimum Cost Path with Alternating Directions II
Medium
Topics
premium lock icon
Companies
Hint
You are given two integers m and n representing the number of rows and columns of a grid, respectively.

The cost to enter cell (i, j) is defined as (i + 1) * (j + 1).

You are also given a 2D integer array waitCost where waitCost[i][j] defines the cost to wait on that cell.

You start at cell (0, 0) at second 1.

At each step, you follow an alternating pattern:

On odd-numbered seconds, you must move right or down to an adjacent cell, paying its entry cost.
On even-numbered seconds, you must wait in place, paying waitCost[i][j].
Return the minimum total cost required to reach (m - 1, n - 1).
"""

from typing import List 
from collections import deque 

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        min_costs = [[float('inf')] * n for _ in range(m)]

        def get_neighbors(i, j):
            neighbors = []
            if i < m - 1:  # move down
                neighbors.append((i + 1, j))
            if j < n - 1:  # move right
                neighbors.append((i, j + 1))
            return neighbors 

        waitCost[m - 1][n - 1] = 0
        min_costs[0][0] = 1
        # queue: (i, j)
        queue = set([(0, 0)])
        while queue:
            # Move right or down
            new_queue = set([])
            for i, j in queue:
                neighbors = get_neighbors(i, j)
                for x, y in neighbors:
                    new_queue.add((x, y))
                    min_costs[x][y] = min(
                        min_costs[x][y], 
                        min_costs[i][j] + (x + 1) * (y + 1) + waitCost[x][y],
                    )
            queue = new_queue
            # # Wait
            # for i, j in queue:
            #     if (i == m - 1 and j == n - 1):
            #         return min_costs[i][j]
            #     min_costs[i][j] += waitCost[i][j]
        print(min_costs)
        return min_costs[m - 1][n - 1]

#  m = 1, n = 2, waitCost = [[1,2]]
m, n, waitCost = 1, 2, [[1,2]]

# m = 2, n = 2, waitCost = [[3,5],[2,4]]
m, n, waitCost = 2, 2, [[3,5],[2,4]]

# m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]]
m, n, waitCost = 2, 3, [[6,1,4],[3,2,5]]

print(Solution().minCost(m, n, waitCost))