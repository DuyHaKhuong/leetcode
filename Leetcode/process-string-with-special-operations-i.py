"""
3612. Process String with Special Operations I
Medium
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
Return the final string result after processing all characters in s.
"""

from typing import List 
from collections import deque 

class Solution:
    def processStr(self, s: str) -> str:
        builder = deque()
        reverse = False 
        for letter in s:
            if letter.isalpha():
                if reverse:
                    builder.appendleft(letter)
                else:
                    builder.append(letter)
            elif letter == '*' and builder:
                if not reverse:
                    builder.pop()
                else:
                    builder.popleft()
            elif letter == '#':
                builder.extend([l for l in builder])
            elif letter == '%':
                reverse = not reverse
        if reverse:
            builder.reverse()
        return ''.join(builder)

s = "a#b%*"
s = "z*#"
print(Solution().processStr(s))