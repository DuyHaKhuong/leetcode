"""
Title: Longest Balanced Substring I
URL: https://leetcode.com/problems/longest-balanced-substring-i/
Difficulty: Medium
Fetched: 2025-10-17 09:52:19

You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the
substring appear the same number of times.

Return the length of the longest balanced substring of s.

Examples:
- Input: s = "abbac"
  Output: 4
  Explanation: The longest balanced substring is "abba" because both 'a' and
  'b' appear exactly 2 times.

- Input: s = "zzabccy"
  Output: 4
  Explanation: The longest balanced substring is "zabc" because 'z', 'a', 'b',
  and 'c' each appear exactly 1 time.

- Input: s = "aba"
  Output: 2
  Explanation: One longest balanced substring is "ab" because 'a' and 'b'
  each appear exactly 1 time. Another is "ba".

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters

Thinking:
freq: l -> count
substring: contiguous segment

count diff: i -> j
"""

from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Returns the length of the longest balanced substring.
        """
        n = len(s)
        if n <= 2:
            return n
        # binary search length
        # low, high = 2, n + 1  # low is known good, high is known bad
        # while high - low > 1:
        #     mid = (low + high + 1) // 2  # low < mid <= high
        #     print(low, mid, high)
        #     for i in range(n - mid + 1):
        #         freq = {}
        #         for l in s[i:i + mid]:
        #             freq[l] = freq.get(l, 0) + 1
        #         counts = set(freq.values())
        #         if len(counts) == 1:
        #             low = mid
        #             break
        #     # cannot find a balanced substring of length mid
        #     if low < mid:
        #         high = mid
        # return low
        # trivial implementation


        max_length = 2
        for length in range(n, 2, -1):
            # print("length = ", length)
            freq_map = None
            for i in range(n - length + 1):
                if not freq_map:
                    freq_map = Counter(s[i:i + length])
                else:
                    l = s[i - 1]
                    freq_map[l] -= 1
                    if freq_map[l] == 0:
                        del freq_map[l]
                    freq_map[s[i + length - 1]] = freq_map.get(s[i + length - 1], 0) + 1
                counts = set(freq_map.values())
                if len(counts) == 1:
                    return length
        return max_length
        # pass

    def check_examples(self) -> None:
        # Example 1
        # print(self.longestBalanced("abbac"))    # Expected: 4
        # # Example 2
        # print(self.longestBalanced("zzabccy"))  # Expected: 4
        # # Example 3
        # print(self.longestBalanced("aba"))      # Expected: 2
        print(self.longestBalanced("rps"))    # Expected: 3
        print(self.longestBalanced("tqtqss"))    # Expected: 6


if __name__ == "__main__":
    sol = Solution()
    # Run example calls (uncomment to execute):
    sol.check_examples()
    # Or run a single custom call:
    # print(sol.longestBalanced("abbac"))
