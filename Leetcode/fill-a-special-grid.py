"""
3537. Fill a Special Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given a non-negative integer n representing a 2n x 2n grid. You must fill the grid with integers from 0 to 22n - 1 to make it special. A grid is special if it satisfies all the following conditions:

All numbers in the top-right quadrant are smaller than those in the bottom-right quadrant.
All numbers in the bottom-right quadrant are smaller than those in the bottom-left quadrant.
All numbers in the bottom-left quadrant are smaller than those in the top-left quadrant.
Each of its quadrants is also a special grid.
Return the special 2n x 2n grid.

Note: Any 1x1 grid is special.
""" 

from typing import List 
class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[0]]
        sub_grid = self.specialGrid(n - 1)
        k = 1 << (n - 1)
        grid = [[0] * 2 * k for _ in range(2 * k)]
        # Top right quadrant 
        for i in range(k):
            for j in range(k):
                grid[i][j] = sub_grid[i][j] + 3 * k * k
                grid[i][j + k] = sub_grid[i][j] 
                grid[i + k][j] = sub_grid[i][j] + 2 * k * k
                grid[i + k][j + k] = sub_grid[i][j] + k * k
        return grid
                

n = 2
print(Solution().specialGrid(n))