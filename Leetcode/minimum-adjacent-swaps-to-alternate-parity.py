"""
3587. Minimum Adjacent Swaps to Alternate Parity
Medium
Topics
premium lock icon
Companies
Hint
You are given an array nums of distinct integers.

In one operation, you can swap any two adjacent elements in the array.

An arrangement of the array is considered valid if the parity of adjacent elements alternates, meaning every pair of neighboring elements consists of one even and one odd number.

Return the minimum number of adjacent swaps required to transform nums into any valid arrangement.

If it is impossible to rearrange nums such that no two adjacent elements have the same parity, return -1.
"""

from typing import List 
from collections import defaultdict, deque 

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        n_evens, even_diff = 0, 0
        n_odds, odd_diff = 0, 0
        for i, num in enumerate(nums):
            if num % 2 == 0:
                n_evens += 1
                even_diff += abs(i - 2 * (n_evens - 1))
            else:
                n_odds = (i + 1 - n_evens)
                odd_diff += abs(i - 2 * (n_odds - 1))

        if 2 * n_evens == n:
            # Expect 0, 2, 4, ..., n - 2 or 1, 3, 5 ... n - 1
            return min(odd_diff, even_diff)
        elif 2 * n_evens == n + 1:
            # Expect 0, 2, 4, .. n - 1 for even numbers
            return even_diff
        elif 2 * n_evens == n - 1:
            # Expect position 0, 2, 4, .. n - 1 for odd numbers
            return odd_diff
        else:
            return -1

nums = [2,4,6,5,7]
nums = [2,4,5,7]
# nums = [1,2,3] 
# nums = [4,5,6,8]
nums = [286,475,165,315,446]
print(Solution().minSwaps(nums))