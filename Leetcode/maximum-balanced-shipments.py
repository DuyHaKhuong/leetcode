"""
LeetCode: Maximum Balanced Shipments
URL: https://leetcode.com/problems/maximum-balanced-shipments/
Difficulty: Medium
Fetched: 2025-09-30 13:37:27

Description:
You are given an integer array weight of length n, where weight[i] is the weight of
the i-th parcel arranged in a line. A shipment is a contiguous subarray of parcels.
A shipment is balanced if the weight of its last parcel is strictly less than the
maximum weight among all parcels in that shipment.

Select a set of non-overlapping, contiguous, balanced shipments such that each
parcel appears in at most one shipment (parcels may remain unshipped). Return the
maximum possible number of balanced shipments that can be formed.

Examples:
- Example 1
  Input: weight = [2, 5, 1, 4, 3]
  Output: 2
  Explanation: Choose [2, 5, 1] (max = 5 > last = 1) and [4, 3] (max = 4 > last = 3).

- Example 2
  Input: weight = [4, 4]
  Output: 0
  Explanation: Neither [4] nor [4, 4] is balanced.

Constraints:
- 2 <= n <= 1e5
- 1 <= weight[i] <= 1e9
"""

from typing import *

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        cum_max_numbers = {-1: 0, 0: 0}
        max_queue = []
        for k in range(n):
            while max_queue and weight[k] >= weight[max_queue[-1]]:
                max_queue.pop()
            if max_queue:
                i = max_queue[-1]
                max_num = 1 + cum_max_numbers[i - 1]
                cum_max_numbers[k] = max(cum_max_numbers[k - 1], max_num)
            else:
                cum_max_numbers[k] = cum_max_numbers[k - 1]
            max_queue.append(k)
        return cum_max_numbers[n - 1]

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    # print(sol.maxBalancedShipments([2, 5, 1, 4, 3]), 2)
    # Example 2
    # print(sol.maxBalancedShipments([4, 4]), 0)
    # weights = [625,467,752]
    weights = [1000,999,998]
    print(sol.maxBalancedShipments(weights), "123")
