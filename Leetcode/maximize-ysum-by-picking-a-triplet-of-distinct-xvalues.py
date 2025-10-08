"""
3572. Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
Medium
premium lock icon
Companies
Hint
You are given two integer arrays x and y, each of length n. You must choose three distinct indices i, j, and k such that:

x[i] != x[j]
x[j] != x[k]
x[k] != x[i]
Your goal is to maximize the value of y[i] + y[j] + y[k] under these conditions. Return the maximum possible sum that can be obtained by choosing such a triplet of indices.

If no such triplet exists, return -1.
"""

from typing import List

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        # Find max value of y for each x[i] 
        max_y = {}
        for xval, yval in zip(x, y):
            if xval >= max_y.get(xval, float('-inf')):
                max_y[xval] = yval 
        for i in range(len(x)):
            if x[i] not in max_y:
                max_y[x[i]] = y[i]
            else:
                max_y[x[i]] = max(max_y[x[i]], y[i])
        
        sorted_y = sorted(max_y.values())
        if len(sorted_y) < 3:
            return -1
        return sorted_y[-1] + sorted_y[-2] + sorted_y[-3]