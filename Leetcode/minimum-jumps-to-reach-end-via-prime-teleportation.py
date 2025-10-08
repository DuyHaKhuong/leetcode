"""
Title: Minimum Jumps to Reach End via Prime Teleportation
URL: https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/
Difficulty: Medium
Fetched: 2025-09-28 07:59:45

Description:
You are given an integer array nums of length n. You start at index 0, and the
goal is to reach index n - 1. From an index i, you can perform:

- Adjacent Step: Move to i + 1 or i - 1, if within bounds.
- Prime Teleportation: If nums[i] is prime p, you may instantly jump to any
  index j != i such that nums[j] % p == 0.

Return the minimum number of jumps to reach index n - 1.

Examples:
- Input: nums = [1, 2, 4, 6]
  Output: 2
  Explanation: Step 0 -> 1; teleport (prime 2) 1 -> 3.

- Input: nums = [2, 3, 4, 7, 9]
  Output: 2
  Explanation: Step 0 -> 1; teleport (prime 3) 1 -> 4.

- Input: nums = [4, 6, 5, 8]
  Output: 3
  Explanation: No useful teleports; move 0 -> 1 -> 2 -> 3.

Constraints:
- 1 <= n == nums.length <= 1e5
- 1 <= nums[i] <= 1e6
"""

from typing import *
import numpy as np
import math
from collections import defaultdict, deque


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        """BFS over indices with prime-factor teleportation; O(n log A) typical.

        Implement the logic in LeetCode. This stub is provided per repository guidelines.
        """
        n = len(nums)
        if n == 1:
            return 0

        N = max(nums) + 1
        is_prime = self.sieve(N)
        indices = {}
        for i, num in enumerate(nums):
            indices.setdefault(num, []).append(i)

        def _get_neighbors(i):
            nodes = set()
            if i > 0:
                nodes.add(i - 1)
            if i < n - 1:
                nodes.add(i + 1)
            if is_prime[nums[i]]:
                p = nums[i]
                # We need p -> list of indices j where nums[j] % p == 0
                for k in range(p, N + 1, p):
                    if k in indices:
                        nodes.update(indices[k])
            return sorted(nodes, reverse=True)

        queue = deque([0])
        visited = np.zeros(n, dtype=bool)
        visited[0] = True
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                for node in _get_neighbors(i):
                    if node == n - 1:
                        return steps + 1
                    if not visited[node]:
                        visited[node] = True
                        queue.append(node)
            steps += 1
        return -1  # Should not happen if input is valid

    @classmethod
    def sieve(cls, N):
        is_prime = np.ones(N, dtype=bool)
        is_prime[:2] = False
        for p in range(2, int(math.isqrt(N)) + 1):
            if not is_prime[p]:
                continue
            # p is prime
            is_prime[p*p::p] = False
        return is_prime


if __name__ == "__main__":
    sol = Solution()
    # Example 1
    nums = [1, 2, 4, 6]
    # nums = [2, 3, 4, 7, 9]
    # nums = [2,3,4,7,9]
    # nums = [4, 6, 5, 8]
    # nums = [7,5,7]
    # nums = [7, 4, 3]
    print(nums, sol.minJumps(nums))
    # Example 2
    # self.assertEqual(sol.minJumps([2, 3, 4, 7, 9]), 2)
    # # Example 3
    # self.assertEqual(sol.minJumps([4, 6, 5, 8]), 3)
