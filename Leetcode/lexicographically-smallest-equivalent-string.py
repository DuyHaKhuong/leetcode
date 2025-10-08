"""
1061. Lexicographically Smallest Equivalent String
Medium
Topics
premium lock icon
Companies
Hint
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
"""

from typing import List
import string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Find groups of equivalent characters
        # Get mapping l1 -> l2
        mapping = {l: set() for l in string.ascii_lowercase}
        for (l1, l2) in zip(s1, s2):
            mapping[l1].add(l2)
            mapping[l2].add(l1)

        groups = []
        for l in string.ascii_lowercase:
            group = set(l)
            queue = [l]
            while queue:
                new_queue = []
                for letter in queue:
                    for neighbor in mapping.pop(letter, []):
                        group.add(neighbor)
                        new_queue.append(neighbor)
                queue = new_queue
            groups.append(group)
        
        lowest_equivalent = {}
        for l in string.ascii_lowercase:
            lowest_equivalent[l] = l
            for group in groups:
                if l in group:
                    lowest_equivalent[l] = min(group)
                    break
        
        return ''.join(lowest_equivalent[l] for l in baseStr)

            
                
                
                
            
            