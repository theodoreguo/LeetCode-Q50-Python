# coding=utf-8
"""
Question:
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differs by more than 1.
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n2) runtime, O(n) stack space – Brute force top-down recursion
class Solution:
    def is_balanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1 \
               and self.is_balanced(root.left) \
               and self.is_balanced(root.right)

    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    result = Solution().is_balanced(root)
    print result

    root.left.left = TreeNode(2)
    result = Solution().is_balanced(root)
    print result
