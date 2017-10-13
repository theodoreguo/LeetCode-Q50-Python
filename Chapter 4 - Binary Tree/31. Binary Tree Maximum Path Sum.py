# coding=utf-8
"""
Question:
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the 
parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,
   1
  / \
 2   3
Return 6.

Example Questions Candidate Might Ask:
Q: What if the tree is empty?
A: Assume the tree is non-empty.
Q: How about a tree that contains only a single node?
A: Then the maximum path sum starts and ends at the same node.
Difficulty: Hard, Frequency: Medium
Q: What if every node contains negative value?
A: Then you should return the single node value that is the least negative.
Q: Does the maximum path have to go through the root node?
A: Not necessarily. For example, the below tree yield 6 as the maximum path sum and does not go through root.
     -5
     / \
    2   3
   / \
 -1   4
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
O(n) runtime, O(n) space

Anytime when you found that doing top down approach uses a lot of repeated calculation, bottom up approach usually is 
able to be more efficient.
           __Node__
          /        \
 left subtree    right subtree
 
Try the bottom up approach. At each node, the potential maximum path could be one of these cases:
i. max(left subtree) + node
ii. max(right subtree) + node
iii. max(left subtree) + max(right subtree) + node
iv. the node itself

Then, we need to return the maximum path sum that goes through this node and to either one of its left or right subtree 
to its parent. 
There’s a little trick here: If this maximum happens to be negative, we should return 0, which means: “Do not include 
this subtree as part of the maximum path of the parent node”, which greatly simplifies our code.
"""

# O(n) runtime, O(log n) space – Recursion
class Solution:
    maxSum = float("-inf")

    def max_path_sum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.find_max(root)
        return self.maxSum

    def find_max(self, p):
        if not p:
            return 0

        left = self.find_max(p.left)
        right = self.find_max(p.right)
        self.maxSum = max(p.val + left + right, self.maxSum)
        result = p.val + max(left, right)
        return result if result else 0

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print Solution().max_path_sum(root)
