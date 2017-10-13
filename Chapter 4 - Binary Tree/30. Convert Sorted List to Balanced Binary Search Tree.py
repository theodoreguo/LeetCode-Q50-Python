# coding=utf-8
"""
Question:
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Hint:
Things get a little more complicated when you have a singly linked list instead of an array. Please note that in linked
list, you no longer have random access to an element in O(1) time.
How about inserting nodes following the list’s order? If we can achieve this, we no longer need to find the middle
element, as we are able to traverse the list while inserting nodes to the tree.
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
O(n) runtime, O(log n) stack space – Bottom-up recursion

Note that the algorithm requires the list’s length to be passed in as the function’s parameters. The list’s length could 
be found in O(n) time by traversing the entire list’s once. The recursive calls traverse the list and create tree’s 
nodes by the list’s order, which also takes O(n) time. Therefore, the overall run time complexity is still O(n).
"""
class Solution:
    list = None

    def sorted_list_to_BST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
        self.list = head
        return self._sorted_list_to_BST(0, n - 1)

    def _sorted_list_to_BST(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: TreeNode
        """
        if start > end:
            return None

        mid = (start + end) / 2
        leftChild = self._sorted_list_to_BST(start, mid - 1)
        parent = TreeNode(self.list.val)
        parent.left = leftChild
        self.list = self.list.next
        parent.right = self._sorted_list_to_BST(mid + 1, end)
        return parent

"""
O(n log n) runtime, O(log n) stack space

It's recursive BST construction using slow-fast traversal on the linked list to get the middle element and make that the 
root. Left side of the list forms left sub-tree and right side of the middle element forms the right sub-tree.
"""
class Solution2:
    def sorted_list_to_BST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = not fast.next.next
            prev = slow
            slow = slow.next
        root = TreeNode(slow.val)
        if prev:
            prev.next = None
        else:
            head = None
        root.left = self.sorted_list_to_BST(head)
        root.right = self.sorted_list_to_BST(slow.next)
        return root

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    result = Solution().sorted_list_to_BST(head)
    # result = Solution2().sorted_list_to_BST(head)
    print result.val
    print result.left.val
    print result.right.val
