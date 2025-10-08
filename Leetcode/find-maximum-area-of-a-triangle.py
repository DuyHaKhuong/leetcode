"""
3588. Find Maximum Area of a Triangle
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D array coords of size n x 2, representing the coordinates of n points in an infinite Cartesian plane.

Find twice the maximum area of a triangle with its corners at any three elements from coords, such that at least one side of this triangle is parallel to the x-axis or y-axis. Formally, if the maximum area of such a triangle is A, return 2 * A.

If no such triangle exists, return -1.

Note that a triangle cannot have zero area.
"""

from typing import List 
from collections import defaultdict 

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        return self.maxAreaX(coords)

    def maxAreaX(self, coords: List[List[int]]) -> int:
        # Sort by x axis 
        max_y_points = {}
        min_y_points = {}

        max_x_points = {}
        min_x_points = {}
        pos, neg = float('inf'), float('-inf')

        max_x, min_x = neg, pos
        max_y, min_y = neg, pos
        for x, y in coords:
            if y > max_y_points.get(x, neg):
                max_y_points[x] = y 
                max_y = max(max_y, y)
            if y < min_y_points.get(x, pos):
                min_y_points[x] = y 
                min_y = min(min_y, y)

            if x > max_x_points.get(y, neg):
                max_x_points[y] = x 
                max_x = max(max_x, x)
            if x < min_x_points.get(y, pos):
                min_x_points[y] = x 
                min_x = min(min_x, x)
        
        max_area = -1
        for x in max_y_points:
            base = max_y_points[x] - min_y_points[x]
            height = max(max_x - x, x - min_x)
            max_area = max(max_area, base * height)

        for y in max_x_points:
            base = max_x_points[y] - min_x_points[y]
            height = max(max_y - y, y - min_y)
            max_area = max(max_area, base * height)
        return max_area if max_area > 0 else -1

coords = [[1,1],[1,2],[3,2],[3,3]]
# coords = [[1,1],[2,2],[3,3]]
print(Solution().maxArea(coords))

