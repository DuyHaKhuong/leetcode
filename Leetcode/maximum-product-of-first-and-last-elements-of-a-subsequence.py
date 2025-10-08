"""
3584. Maximum Product of First and Last Elements of a Subsequence
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer m.

Return the maximum product of the first and last elements of any subsequence of nums of size m.
"""

from typing import List 

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        min_val, max_val = float('inf'), float('-inf')
        max_prod = float('-inf')
        for i, num in enumerate(nums):
            if i + m > len(nums):
                break
            min_val, max_val = min(num, min_val), max(num, max_val)
            max_prod = max(
                max_prod,
                min_val * nums[i + m - 1],
                max_val * nums[i + m - 1],
            )
        return max_prod


nums, m = [1,3,-5,5,6,-4], 3
nums, m = [2,-1,2,-6,5,2,-5,7], 2 
print(Solution().maximumProduct(nums, m))