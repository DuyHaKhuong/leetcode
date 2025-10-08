"""
LeetCode: House Robber III
URL: https://leetcode.com/problems/house-robber-iii/
Difficulty: Medium
Fetched: 2025-10-05 21:30:17

Description:
You are given the root of a binary tree where each node represents a house with some
amount of money. If two directly-connected houses are robbed on the same night, the
police are alerted. Return the maximum amount of money that can be robbed without
alerting the police.

Examples:
- Example 1
  Input: root = [3, 2, 3, null, 3, null, 1]
  Output: 7
  Explanation: Rob nodes with values 3, 3, and 1.

- Example 2
  Input: root = [3, 4, 5, 1, 3, null, 1]
  Output: 9
  Explanation: Rob nodes with values 4 and 5.

Constraints:
- 1 <= number of nodes <= 1e4
- 0 <= Node.val <= 1e4
"""

from typing import *
from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, tree_root: Optional[TreeNode]) -> int:

        @lru_cache(None)
        def _rob_without_root(r):
            if r.left is None and r.right is None:
                return 0
            value = 0
            if r.left:
                value = max(
                    _rob_with_root(r.left),
                    _rob_without_root(r.left)
                )
            if r.right:
                value += max(
                    _rob_with_root(r.right),
                    _rob_without_root(r.right)
                )
            return value

        @lru_cache(None)
        def _rob_with_root(root):
            if root is None:
                return 0
            value = root.val
            if root.left:
                value += _rob_without_root(root.left)
            if root.right:
                value += _rob_without_root(root.right)
            return value

        # max value with root
        # max value without root
        return max(
            _rob_with_root(tree_root),
            _rob_without_root(tree_root),
        )

if __name__ == "__main__":
    # Code to run examples (not tests)
    # Helper to build tree from level-order list with None for null
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def build_tree(levels: List[Optional[int]]) -> Optional[TreeNode]:
        if not levels:
            return None
        it = iter(levels)
        root_val = next(it)
        if root_val is None:
            return None
        root = TreeNode(root_val)
        queue = [root]
        for a, b in zip(it, it):
            node = queue.pop(0)
            if a is not None:
                node.left = TreeNode(a)
                queue.append(node.left)
            if b is not None:
                node.right = TreeNode(b)
                queue.append(node.right)
        return root

    sol = Solution()
    # print(sol.rob(build_tree([3, 2, 3, None, 3, None, 1])))   # Expected: 7
    print(sol.rob(build_tree([3, 4, 5, 1, 3, None, 1])))      # Expected: 9
