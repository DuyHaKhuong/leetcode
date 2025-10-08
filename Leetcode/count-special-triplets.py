"""
3583. Count Special Triplets
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A special triplet is defined as a triplet of indices (i, j, k) such that:

0 <= i < j < k < n, where n = nums.length
nums[i] == nums[j] * 2
nums[k] == nums[j] * 2
Return the total number of special triplets in the array.

Since the answer may be large, return it modulo 109 + 7.
""" 

"""
Count # (i, j): nums[i] == nums[j] * 2
Map: j -> list of indices i: nums[i] == nums[j] * 2 -> counting 
""" 

from typing import List 
from collections import defaultdict 

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        inverted_map = defaultdict(int)
        for num in nums:
            inverted_map[num] += 1
        print(inverted_map)

        current_map = defaultdict(int)
        total = 0
        for num in nums:
            key = 2 * num 
            if not key in inverted_map:
                current_map[num] += 1 
                continue 
            i_count = current_map[key]
            k_count = inverted_map[key] - current_map[key] - (num == 0)
            total = (total + i_count * k_count) % MOD
            print(num, key, current_map, total)
            current_map[num] += 1 
        return total 
            



nums = [6,3,6]
# print(Solution().specialTriplets(nums))
nums = [0,1,0,0]
# nums = [84,2,93,1,2,2,26]
print(Solution().specialTriplets(nums))