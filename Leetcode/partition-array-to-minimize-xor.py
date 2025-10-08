"""
3599. Partition Array to Minimize XOR
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k.

Your task is to partition nums into k non-empty subarrays. For each subarray, compute the bitwise XOR of all its elements.

Return the minimum possible value of the maximum XOR among these k subarrays.
""" 

from typing import List 

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_vals = [None] * n
        min_vals[0] = nums[0]
        for j in range(1, n):
            min_vals[j] = min_vals[j - 1] ^ nums[j]
        # print(dq[1])
        for i in range(2, k + 1):
            # Compute dq[i] from dq[i - 1]
            next_vals = [None] * n 
            for j in range(i - 1, n):
                # compute dq[i][j]
                min_val = float('inf')
                val = 0
                for l in range(j, i - 2, -1):
                    val = val ^ nums[l]
                    max_value = max(val, min_vals[l - 1])
                    min_val = min(min_val, max_value)

                next_vals[j] = min_val
            min_vals = next_vals[:]
            # print(i, dq[i])

        return min_vals[n - 1]


nums, k = [1,2,3], 2
nums, k = [1,1,2,3,1], 2
nums, k = [2,3,3,2], 3
nums, k = [772,991,1088,1399,1719,595,952,758,1444,825], 5
print(Solution().minXor(nums, k))