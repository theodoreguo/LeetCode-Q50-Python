# coding=utf-8
"""
Question:
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Hint:
This question is highly recursive in nature. Think of how binary search works.
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) runtime, O(log n) stack space – Divide and conquer
class Solution:
    def sorted_array_to_BST(self, nums):
        """
        :type nums: [int]
        :rtype: TreeNode
        """
        return self._sorted_array_to_BST(nums, 0, len(nums) - 1)

    def _sorted_array_to_BST(self, nums, start, end):
        """
        :type nums: [int]
        :type start: int
        :type end: int
        :rtype: TreeNode
        """
        if start > end:
            return None

        mid = (start + end) / 2
        node = TreeNode(nums[mid])
        node.left = self._sorted_array_to_BST(nums, start, mid - 1)
        node.right = self._sorted_array_to_BST(nums, mid + 1, end)
        return node

if __name__ == '__main__':
    num = [1, 2, 3]
    result = Solution().sorted_array_to_BST(num)
    print result.val
    print result.left.val
    print result.right.val
