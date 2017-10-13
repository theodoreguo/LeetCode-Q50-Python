# coding=utf-8
"""
Question:
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same
parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf
nodes. Return the new root.

For example:
Given a binary tree [1, 2, 3, 4, 5],
     1
    / \
   2   3
  / \
 4   5
return the root of the binary tree [4, 5, 2, #, #, 3, 1].
     4
    / \
   5   2
      / \
     3   1

Hint:
At each node you want to assign:
p.left = parent.right
p.right = parent
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
O(n) runtime, O(1) space - Top-down approach

We need to be very careful when reassigning current node’s left and right children. Besides making a copy of the parent
node, you would also need to make a copy of the parent’s right child, too. The reason is the current node becomes the 
parent node in the next iteration.
"""
class Solution:
    def upside_down_binary_tree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        p, parent, parent_right = root, None, None
        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left
        return parent

"""
O(n) runtime, O(n) space - Bottom-up approach

If we reassign the bottom-level nodes before the upper ones, we won’t have to make copies and worry about overwriting 
something. We know the new root will be the left-most leaf node, so we begin the reassignment here.
"""
class Solution2:
    def upside_down_binary_tree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.bottom_up(root, None)

    def bottom_up(self, p, parent):
        if p is None:
            return parent
        root = self.bottom_up(p.left, p)
        p.left = parent if parent is None else parent.right
        p.right = parent
        return root

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    result = Solution().upside_down_binary_tree(root)
    # result = Solution2().upside_down_binary_tree(root)
    print result.val
    print result.left.val
    print result.right.val
    print result.right.left.val
    print result.right.right.val
