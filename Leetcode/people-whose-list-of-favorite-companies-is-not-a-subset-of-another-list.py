"""
LeetCode: People Whose List of Favorite Companies Is Not a Subset of Another List
URL: https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
Difficulty: Medium
Fetched: 2025-10-06 09:51:59

Description:
You are given an array favoriteCompanies where favoriteCompanies[i] is the list of
favorite companies for the i-th person (0-indexed). Return the indices of people
whose list is not a subset of any other person's list. Return the indices in
increasing order.

Examples:
- Example 1
  Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
  Output: [0, 1, 4]
  Explanation: Lists at indices 2 and 3 are subsets of others; 0, 1, and 4 are not.

- Example 2
  Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
  Output: [0, 1]
  Explanation: Index 2 is a subset of index 0.

- Example 3
  Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
  Output: [0, 1, 2, 3]

Constraints:
- 1 <= favoriteCompanies.length <= 100
- 1 <= favoriteCompanies[i].length <= 500
- 1 <= favoriteCompanies[i][j].length <= 20
- All strings within favoriteCompanies[i] are distinct
- All lists are distinct after sorting (favoriteCompanies[i] != favoriteCompanies[j])
- Strings contain only lowercase English letters

Thinking: not a subset? encode in bits?
company -> index

"""

from typing import *

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        results = []
        company_sets = {
            i: set(companies) for i, companies in enumerate(favoriteCompanies)
        }
        n = len(favoriteCompanies)
        for i, companies in company_sets.items():
            is_subset = False
            for j in range(n):
                other_companies = company_sets[j]
                if i != j and companies.issubset(other_companies):
                    is_subset = True
                    break
            if not is_subset:
                results.append(i)
        return results

if __name__ == "__main__":
    # Code to run examples (not tests)
    sol = Solution()
    print(sol.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))  # Expected: [0, 1, 4]
    print(sol.peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))  # Expected: [0, 1]
    print(sol.peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]))  # Expected: [0, 1, 2, 3]
