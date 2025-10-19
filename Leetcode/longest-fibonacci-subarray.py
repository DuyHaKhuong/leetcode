"""
Title: Longest Fibonacci Subarray
URL: https://leetcode.com/problems/longest-fibonacci-subarray/
Difficulty: Medium
Fetched: 2025-10-16 10:31:59

You are given an array of positive integers nums.

A Fibonacci array is a contiguous sequence where every term from the third
onward equals the sum of the two preceding terms.

Return the length of the longest Fibonacci subarray in nums.

Note: Subarrays of length 1 or 2 are always Fibonacci.

Examples:
- Input: nums = [1, 1, 1, 1, 2, 3, 5, 1]
  Output: 5
  Explanation: The longest Fibonacci subarray is nums[2..6] = [1, 1, 2, 3, 5].
  It is Fibonacci because 1 + 1 = 2, 1 + 2 = 3, and 2 + 3 = 5.

- Input: nums = [5, 2, 7, 9, 16]
  Output: 5
  Explanation: The longest Fibonacci subarray is nums[0..4] = [5, 2, 7, 9, 16].
  It is Fibonacci because 5 + 2 = 7, 2 + 7 = 9, and 7 + 9 = 16.

- Input: nums = [1000000000, 1000000000, 1000000000]
  Output: 2
  Explanation: The longest Fibonacci subarray is nums[1..2] = [1000000000, 1000000000].
  Any subarray of length 2 is Fibonacci.

Constraints:
- 3 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        a1, a2 = nums[0], nums[1]
        current_length = 2 # current length starting from a1
        max_length = 2
        for i in range(2, n):
            a3 = nums[i]
            if a1 + a2 != a3:
                current_length = 2
            else:
                current_length += 1
                # print(a1, a2, a3, current_length)
                max_length = max(
                    max_length,
                    current_length,
                )
            a1, a2 = a2, a3
        return max_length

    def check_examples(self) -> None:
        # Example 1
        print(self.longestSubarray([1, 1, 1, 1, 2, 3, 5, 1]))  # Expected: 5
        # Example 2
        print(self.longestSubarray([5, 2, 7, 9, 16]))  # Expected: 5
        # Example 3
        print(self.longestSubarray([1000000000, 1000000000, 1000000000]))  # Expected: 2


if __name__ == "__main__":
    sol = Solution()
    # Run example calls (uncomment to execute):
    # sol.check_examples()
    # Or run a single custom call:
    print(sol.longestSubarray([1, 1, 1, 1, 2, 3, 5, 1]))
