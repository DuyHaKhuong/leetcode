"""
Title: Split Array With Minimum Difference
URL: https://leetcode.com/problems/split-array-with-minimum-difference/
Difficulty: Medium
Fetched: 2025-10-07

Description:
Given an integer array nums, split it into exactly two non-empty subarrays,
left and right, by choosing an index i (0 <= i < n - 1) such that
left = nums[0..i] is strictly increasing and right = nums[i+1..n-1] is strictly decreasing.
Return the minimum possible absolute difference between sum(left) and sum(right).
If no valid split exists, return -1.

Examples:
- Input: nums = [1, 3, 2]
  Output: 2
  Explanation: Valid splits include i = 0 -> left = [1], right = [3, 2] (valid);
  i = 1 -> left = [1, 3], right = [2] (valid). The minimum absolute difference of sums is 2.

- Input: nums = [1, 2, 4, 3]
  Output: 4
  Explanation: Valid splits at i = 1 and i = 2 yield differences 4 and 4; minimum is 4.

- Input: nums = [3, 1, 2]
  Output: -1
  Explanation: No index i produces left strictly increasing and right strictly decreasing.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = 0
        total = 0
        prev_value = float('-inf')
        for i, num in enumerate(nums):
            if num > prev_value:
                prev_value = num
                current_sum += num
                continue
            # When num <= prev_value, the right array must start from prev_value or num
            # First, check if the rest is strictly decreasing
            total = current_sum + num
            for j in range(i + 1, n):
                total += nums[j]
                if nums[j] >= nums[j - 1]:
                    return -1

            if num == prev_value:
                # The right array must start from index i (num)
                return abs(total - 2 * current_sum)

            # When num < prev_value, the right array must start from
            # index i (num) or index i - 1 (prev_value)
            remaining_sum = total - current_sum
            return min(
                abs(remaining_sum - current_sum),
                abs(remaining_sum - current_sum + 2 * prev_value),
            )
        return abs(total - 2 * nums[-1])

    def check_examples(self) -> None:
        # Example 1
        # print(self.splitArray([1, 3, 2]))  # Expected: 2

        # Example 2
        # print(self.splitArray([1, 2, 4, 3]))  # Expected: 4

        # Example 3
        # print(self.splitArray([3, 1, 2]))  # Expected: -1
        # nums = [2,4]
        nums = [6,7,3]
        print(self.splitArray(nums))  # Expected: 2
        return


if __name__ == "__main__":
    sol = Solution()
    # Quick run with Example 1 (uncomment to execute):
    # print(sol.splitArray([1, 3, 2]))
    sol.check_examples()
