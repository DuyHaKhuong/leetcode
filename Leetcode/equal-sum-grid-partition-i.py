"""
3546. Equal Sum Grid Partition I
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.
"""

from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        # check horizontal partition 
        s = 0 
        for i in range(m):
            s += sum(grid[i])
            if s * 2 == total:
                return True 
        
        # check vertical partition 
        s = 0 
        for j in range(n):
            s += sum(grid[i][j] for i in range(m))
            if s * 2 == total:
                return True 
        return False
