"""
3552. Grid Teleportation Traversal
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D character grid matrix of size m x n, represented as an array of strings, where matrix[i][j] represents the cell at the intersection of the ith row and jth column. Each cell is one of the following:

'.' representing an empty cell.
'#' representing an obstacle.
An uppercase letter ('A'-'Z') representing a teleportation portal.
You start at the top-left cell (0, 0), and your goal is to reach the bottom-right cell (m - 1, n - 1). You can move from the current cell to any adjacent cell (up, down, left, right) as long as the destination cell is within the grid bounds and is not an obstacle.

If you step on a cell containing a portal letter and you haven't used that portal letter before, you may instantly teleport to any other cell in the grid with the same letter. This teleportation does not count as a move, but each portal letter can be used at most once during your journey.

Return the minimum number of moves required to reach the bottom-right cell. If it is not possible to reach the destination, return -1.
"""

import string 
from typing import List

def get_neighbors(i, j, m, n):
    neighbors = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ]
    return [(x, y) for x, y in neighbors if 0 <= x < m and 0 <= y < n]

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        letter_cells = {l: [] for l in string.ascii_uppercase}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] not in (".", "#"):
                    l = matrix[i][j]
                    letter_cells[l].append((i, j))
        
        distances = [[-1] * n for _ in range(m)]
        d = 0
        distances[0][0] = 0
        queue = [(0, 0)]
        
        while queue:
            # print(queue)
            # Expand the queue to cells with the same upper letter 
            letters = set([matrix[i][j] for i, j in queue if matrix[i][j] in string.ascii_uppercase])
            for l in letters:
                for px, py in letter_cells[l]:
                    if distances[px][py] != -1:
                        continue
                    distances[px][py] = d
                    queue.append((px, py))

            d += 1
            new_queue = []
            for i, j in queue:
                # print(i, j, d, get_neighbors(i, j, m, n))
                for x, y in get_neighbors(i, j, m, n):
                    if matrix[x][y] == "#":
                        continue
                    # Check if the cell is already visited
                    if distances[x][y] != -1:
                        continue
                    # Add the cell to the queue
                    new_queue.append((x, y))
                    distances[x][y] = d
            queue = new_queue
        return distances[m - 1][n - 1]


m = [
    "..",
    "HA",
    ".C",
    "A."
]
print(Solution().minMoves(m))