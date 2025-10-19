"""
Title: Maximum Number of Distinct Elements After Operations
URL: https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
Difficulty: Medium
Fetched: 2025-10-18 08:56:55

You are given an integer array nums and an integer k.

You may perform the following operation on each element of the array at most
once: add an integer in the range [-k, k] to that element.

Return the maximum possible number of distinct elements in nums after
performing the operations.

Examples:
- Input: nums = [1, 2, 2, 3, 3, 4], k = 2
  Output: 6
  Explanation: After operations on the first four elements, nums can become
  [-1, 0, 1, 2, 3, 4], which has 6 distinct elements.

- Input: nums = [4, 4, 4, 4], k = 1
  Output: 3
  Explanation: Add -1 to nums[0] and +1 to nums[1], giving [3, 5, 4, 4].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 0 <= k <= 10^9

Thinking:
sort(), then add
"""

from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        """
        Returns the maximum number of distinct elements achievable by adjusting
        each element at most once by a value in [-k, k].
        """
        nums.sort()
        distinct_count = 0
        prev_value = float('-inf')
        for num in nums:
            if num - k > prev_value:
                prev_value = num - k
                distinct_count += 1
            elif num + k >= prev_value + 1:
                prev_value = prev_value + 1
                distinct_count += 1
            else:
                continue
        return distinct_count

    def check_examples(self) -> None:
        # Example 1
        print(self.maxDistinctElements([1, 2, 2, 3, 3, 4], 2))  # Expected: 6
        # Example 2
        print(self.maxDistinctElements([4, 4, 4, 4], 1))        # Expected: 3


if __name__ == "__main__":
    sol = Solution()
    # Run example calls (uncomment to execute):
    sol.check_examples()
    # Or run a single custom call:
    # print(sol.maxDistinctElements([1, 2, 2, 3, 3, 4], 2))
