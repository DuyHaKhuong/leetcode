"""
Title: Split and Merge Array Transformation
URL: https://leetcode.com/problems/split-and-merge-array-transformation/
Difficulty: Medium
Fetched: 2025-10-18 09:37:46

You are given two integer arrays nums1 and nums2, each of length n. You may
perform the following split-and-merge operation on nums1 any number of times:

- Choose a subarray nums1[L..R].
- Remove that subarray, leaving the prefix nums1[0..L-1] (empty if L = 0) and
  the suffix nums1[R+1..n-1] (empty if R = n - 1).
- Re-insert the removed subarray (in its original order) at any position in the
  remaining array (between any two elements, at the start, or at the end).

Return the minimum number of split-and-merge operations needed to transform
nums1 into nums2.

Examples:
- Input: nums1 = [3, 1, 2], nums2 = [1, 2, 3]
  Output: 1
  Explanation: Split out [3] (L = 0, R = 0); remaining is [1, 2]. Insert [3]
  at the end to obtain [1, 2, 3].

- Input: nums1 = [1, 1, 2, 3, 4, 5], nums2 = [5, 4, 3, 2, 1, 1]
  Output: 3
  Explanation:
  1) Remove [1, 1, 2] at indices 0..2; remaining [3, 4, 5]; insert at position 2 -> [3, 4, 1, 1, 2, 5]
  2) Remove [4, 1, 1] at indices 1..3; remaining [3, 2, 5]; insert at position 3 -> [3, 2, 5, 4, 1, 1]
  3) Remove [3, 2] at indices 0..1; remaining [5, 4, 1, 1]; insert at position 2 -> [5, 4, 3, 2, 1, 1]

Constraints:
- 2 <= n == nums1.length == nums2.length <= 10^6
- -10^5 <= nums1[i], nums2[i] <= 10^5
- nums2 is a permutation of nums1
"""

from typing import List


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Returns the minimum number of split-and-merge operations to transform
        nums1 into nums2.
        """
        pass

    def check_examples(self) -> None:
        # Example 1
        print(self.minSplitMerge([3, 1, 2], [1, 2, 3]))
        # Expected: 1
        # Example 2
        print(self.minSplitMerge([1, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 1]))
        # Expected: 3


if __name__ == "__main__":
    sol = Solution()
    # Run example calls (uncomment to execute):
    # sol.check_examples()
    # Or run a single custom call:
    # print(sol.minSplitMerge([3, 1, 2], [1, 2, 3]))
