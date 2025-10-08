"""
3597. Partition String 
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, partition it into unique segments according to the following procedure:

Start building a segment beginning at index 0.
Continue extending the current segment character by character until the current segment has not been seen before.
Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.
Repeat until you reach the end of s.
Return an array of strings segments, where segments[i] is the ith segment created.
"""

from typing import List 

class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments = []
        seen = set()
        current_idx = 0
        num = 0
        for i, l in enumerate(s):
            # print(i, l, num)
            num = (num << 5) + (ord(l) - ord('a') + 1)
            if num not in seen:
                seen.add(num)
                segments.append(s[current_idx: i + 1])
                current_idx = i + 1
                num = 0
        return segments

s = "abbccccd"
# s = "aaaa"
print(Solution().partitionString(s))