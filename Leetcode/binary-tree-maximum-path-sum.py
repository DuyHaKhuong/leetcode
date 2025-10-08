"""
LeetCode: Binary Tree Maximum Path Sum
URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Difficulty: Hard
Fetched: 2025-10-06 10:39:38

Description:
A path in a binary tree is a sequence of nodes where each adjacent pair is connected
by an edge. A node can appear at most once in a path, and the path does not need to
pass through the root. The path sum is the sum of the node values along the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Examples:
- Example 1
  Input: root = [1, 2, 3]
  Output: 6
  Explanation: The optimal path is 2 -> 1 -> 3 with sum 2 + 1 + 3 = 6.

- Example 2
  Input: root = [-10, 9, 20, null, null, 15, 7]
  Output: 42
  Explanation: The optimal path is 15 -> 20 -> 7 with sum 15 + 20 + 7 = 42.

Constraints:
- 1 <= number of nodes <= 3 * 10^4
- -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import *
from functools import lru_cache

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # With root
        @lru_cache(None)
        def _max_path_with_root(node):
            value = node.val
            if node.left:
                value += max(0, _max_single_path_from_root(node.left))
            if node.right:
                value += max(0, _max_single_path_from_root(node.right))
            return value

        @lru_cache(None)
        def _max_single_path_from_root(node):
            values = [0]
            if node.left:
                values.append(_max_single_path_from_root(node.left))
            if node.right:
                values.append(_max_single_path_from_root(node.right))
            return node.val + max(values)

        @lru_cache(None)
        def _max_path(node):
            values = [_max_path_with_root(node)]
            if node.left:
                values.append(_max_path(node.left))
            if node.right:
                values.append(_max_path(node.right))
            return max(values)

        # Without root, either left or right
        return _max_path(root)


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
    print(sol.maxPathSum(build_tree([-3])))                        # Expected: -3
    print(sol.maxPathSum(build_tree([1, 2, 3])))                        # Expected: 6
    print(sol.maxPathSum(build_tree([-10, 9, 20, None, None, 15, 7])))  # Expected: 42
