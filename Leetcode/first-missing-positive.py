"""
41. First Missing Positive
Hard
Topics
premium lock icon
Companies
Hint
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""

from typing import List 

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # The missing number must be from 1 to (n  + 1)
        # Try to put each number in its correct position 
        for i, num in enumerate(nums):
            if num <= 0 or num > n:
                nums[i] = 0
                continue 
            # num is between 1 and n
            idx = num - 1 
            if nums[idx] == num:
                continue 
            