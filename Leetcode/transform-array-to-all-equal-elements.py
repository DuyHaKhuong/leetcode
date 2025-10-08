"""
3576. Transform Array to All Equal Elements
Medium
premium lock icon
Companies
Hint
You are given an integer array nums of size n containing only 1 and -1, and an integer k.

You can perform the following operation at most k times:

Choose an index i (0 <= i < n - 1), and multiply both nums[i] and nums[i + 1] by -1.

Note that you can choose the same index i more than once in different operations.

Return true if it is possible to make all elements of the array equal after at most k operations, and false otherwise.
"""

from typing import List 

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        count = 0 
        prev = 1 
        for i, num in enumerate(nums):
            print(i, num, prev, count)
            if i == len(nums) - 1:
                return count <= k and num == prev
            # Decide to do multiply by -1 or not  
            if num == 1:
                if prev == 1:
                    continue 
                else:
                    count += 1 
                    prev = -1 
            if num == -1:
                if prev == 1:
                    count += 1 
                    prev = -1 
                else:
                    prev = 1
        return count <= k 
        pass


# Input: nums = [1,-1,1,-1,1], k = 3 
# Output: true

# print(Solution().canMakeEqual([1,-1,1,-1,1], 3))
# print(Solution().canMakeEqual([-1,-1,-1,1,1,1], 5))
print(Solution().canMakeEqual([1,-1,1], 2))


