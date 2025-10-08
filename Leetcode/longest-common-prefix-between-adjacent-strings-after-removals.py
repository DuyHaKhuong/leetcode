"""
3598. Longest Common Prefix Between Adjacent Strings After Removals
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:

Remove the element at index i from the words array.
Compute the length of the longest common prefix among all adjacent pairs in the modified array.
Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.
"""

from typing import List 

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:

        def _get_prefix_length(w1, w2):
            l = 0 
            while l < len(w1) and l < len(w2) and w1[l] == w2[l]:
                l += 1 
            return l

        n = len(words)
        if n <= 2:
            return [0] * n 
        prefix_lengths = [0] * n 
        for i in range(1, n):
            w1, w2 = words[i - 1], words[i]
            prefix_lengths[i] = _get_prefix_length(w1, w2)

        # When removing words[i], we remove prefix lengths of 
        # words[i-1], words[i]
        # words[i], words[i+1]
        # and add prefix length of words[i-1], words[i+1]
        # Find max_length_before and max_length_after

        max_length_to = prefix_lengths[:]  # Max prefix length to i: 0, 1, .. i
        max_length_from = [0] * n  # Max prefix length from i: i, i + 1..
        for i in range(1, n):
            max_length_to[i] = max(max_length_to[i - 1], prefix_lengths[i])
        for i in range(n - 2, -1, -1):
            max_length_from[i] = max(max_length_from[i + 1], prefix_lengths[i + 1])
        
        ans = [0] * n 
        # Handle edge case 
        ans[0] = max_length_from[1]
        ans[n - 1] = max_length_to[n - 2]

        # print(max_length_to)
        print(max_length_from)
        for i in range(1, n - 1):
            array = (
                max_length_to[i - 1], 
                max_length_from[i + 1],
                _get_prefix_length(words[i - 1], words[i + 1]),
            )
            print(i, words[i], array)
            ans[i] = max(array)

        return ans
        

            
words = ["jump","run","run","jump","run"]
# words = ["dog","racer","car"]
words = ["fec","fef","acaa","adfa","afc","fdbda"]
words = ["efe","feae","fb"]
print(words)
print(Solution().longestCommonPrefix(words))