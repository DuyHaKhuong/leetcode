"""
LeetCode: Valid Word Abbreviation
URL: https://leetcode.com/problems/valid-word-abbreviation/
Difficulty: Easy
Fetched: 2025-10-05 07:04:35

Description:
Given a non-empty string `word` and an abbreviation `abbr`, determine if `abbr`
validly abbreviates `word`. A valid abbreviation replaces some number of
consecutive letters with their count, and numbers must not have leading zeros.

Examples:
- Example 1
  Input: word = "internationalization", abbr = "i12iz4n"
  Output: true
  Explanation: "internationalization" -> "i" + 12 + "iz" + 4 + "n".

- Example 2
  Input: word = "apple", abbr = "a2e"
  Output: false
  Explanation: Skipping 2 from index 1 lands on 'l', but final 'e' mismatches.

- Example 3
  Input: word = "substitution", abbr = "s10n"
  Output: true
  Explanation: "substitution" -> "s" + 10 + "n".

Constraints:
- 1 <= word.length <= 20
- 1 <= abbr.length <= 20
- word consists of lowercase English letters
- abbr consists of lowercase English letters and digits
- Numbers in abbr cannot have leading zeros
"""

from typing import *


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx_word, idx_abbr = 0, 0
        n_word, n_abbr = len(word), len(abbr)
        while idx_word < n_word and idx_abbr < n_abbr:
            if abbr[idx_abbr].isalpha():
                if word[idx_word] != abbr[idx_abbr]:
                    return False
                idx_word += 1
                idx_abbr += 1
            else:
                if abbr[idx_abbr] == '0':
                    return False
                num_start = idx_abbr
                while idx_abbr < n_abbr and abbr[idx_abbr].isdigit():
                    idx_abbr += 1
                skip_count = int(abbr[num_start:idx_abbr])
                idx_word += skip_count
        return idx_word == n_word and idx_abbr == n_abbr


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_examples(self):
            sol = Solution()
            self.assertEqual(sol.validWordAbbreviation("internationalization", "i12iz4n"), True)
            self.assertEqual(sol.validWordAbbreviation("apple", "a2e"), False)
            self.assertEqual(sol.validWordAbbreviation("substitution", "s10n"), True)

    unittest.main()
