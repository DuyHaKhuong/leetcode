"""
Longest Binary Subsequence Less Than or Equal to K
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
"""

from typing import List 
from functools import cache 

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Subproblem: biggest binary number ending at index i
        @cache
        def get_max_val(max_idx, limit):
            if limit == 0:
                return sum(s[i] == '0' for i in range(max_idx + 1))
            if max_idx <= -1:
                return 0
            # Consider two cases: having s[max_idx] or not  
            # Have s[max_idx]
            if s[max_idx] == '0':
                max_val = get_max_val(max_idx - 1, limit // 2) + 1
            else:
                max_val = get_max_val(max_idx - 1, (limit - 1) // 2) + 1
            # Not have s[max_idx]
            max_val = max(
                max_val,
                get_max_val(max_idx - 1, limit)
            )
            return max_val 
        return get_max_val(len(s) - 1, k)


s, k = "1001010", 5
# s, k = "00101001", 1
s, k = "001010101011010100010101101010010", 93951055
print(Solution().longestSubsequence(s, k))