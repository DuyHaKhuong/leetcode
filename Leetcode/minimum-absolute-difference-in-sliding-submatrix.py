"""
3567. Minimum Absolute Difference in Sliding Submatrix
Medium
premium lock icon
Companies
Hint
You are given an m x n integer matrix grid and an integer k.

For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.

Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.

Note: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
""" 

from typing import List

class Solution:

    def _grid_gen(self, a, b):
        for i in range(a):
            for j in range(b):
                yield (i, j)

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Consider submatrix i, j, i + k - 1, j + k - 1 
                values = set(
                    grid[x][y] 
                    for x in range(i, i + k)
                    for y in range(j, j + k)
                    if x < m and y < n
                )
                values = sorted(values)
                if values:
                    min_diff = min(
                        values[i + 1] - values[i]
                        for i in range(len(values) - 1)
                    )
                else:
                    min_diff = 0
                ans[i][j] = min_diff
        return ans

grid = [[3,-1]]
k = 1

grid = [
    [-42305,24053],
    [38028,-20051]
]
k = 2
print(Solution().minAbsDiff(grid, k))