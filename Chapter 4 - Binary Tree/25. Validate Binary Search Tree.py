# coding=utf-8
"""
Question:
Given a binary tree, determine if it is a valid Binary Search Tree (BST).

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
   2
  / \
 1   3
Binary tree [2,1,3], return true.

Example 2:
   1
  / \
 2   3
Binary tree [1,2,3], return false.

Example 3:
  10
  / \
 5  15
    / \
   6   20
It’s obvious that this is not a valid BST, since (6) could never be on the right of (10).
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) runtime, O(n) stack space – Top-down recursion
class Solution(object):
    def is_valid_BST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(p, low, high):
            """
            :type p: TreeNode
            :type low: float
            :type high: float
            :rtype bool
            """
            if not p:
                return True
            return p.val > low and p.val < high and valid(p.left, low, p.val) and valid(p.right, p.val, high)

        return valid(root, float("-inf"), float("inf"))

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print Solution().is_valid_BST(root)
