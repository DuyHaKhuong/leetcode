"""
LeetCode: Longest Subsequence With Non-Zero Bitwise XOR
URL: https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/
Difficulty: Medium
Fetched: 2025-10-07 10:49:36

Description:
You are given an integer array nums. Return the length of the longest subsequence in
nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

Examples:
- Example 1
  Input: nums = [1, 2, 3]
  Output: 2
  Explanation: One longest subsequence is [2, 3] since 2 XOR 3 = 1 (non-zero).

- Example 2
  Input: nums = [2, 3, 4]
  Output: 3
  Explanation: The subsequence [2, 3, 4] has XOR 2 XOR 3 XOR 4 = 5 (non-zero).

Constraints:
- 1 <= nums.length <= 1e5
- 0 <= nums[i] <= 1e9

Thinking: a ^ b ^ c = a ^ (b ^ c)
a ^ a = 0
0 ^ a = a

cum_xor = [..]
cum_xor[i] ^ cum_xor[j] = nums[i + 1] ^ ... ^ nums[j]
for each i, find max j: cum_xor[j] != cum_xor[i]
"""

from typing import *


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        cum_xor = [0] * (n + 1)
        cum_xor[0] = 0
        for i in range(n):
            cum_xor[i + 1] = cum_xor[i] ^ nums[i]

        # if cum_xor[-1] != 0:
        #     return n

        print(cum_xor)
        max_length = 0
        for i in range(n):
            if i > 0 and cum_xor[i] == cum_xor[i - 1]:
                continue
            for j in range(n, i, -1):
                if cum_xor[i] != cum_xor[j]:
                    max_length = max(max_length, j - i)
                    break
        return max_length

if __name__ == "__main__":
    # Code to run examples (not tests)
    sol = Solution()
    # nums = [1,1]
    nums = [0,0,7,0,0,0,7,0,0]
    print(sol.longestSubsequence(nums))  # Expected: 1
    # print(sol.longestSubsequence([1, 2, 3]))  # Expected: 2
    # print(sol.longestSubsequence([2, 3, 4]))  # Expected: 3
