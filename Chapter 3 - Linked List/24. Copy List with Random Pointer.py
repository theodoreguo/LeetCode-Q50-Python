# coding=utf-8
"""
Question:
A linked list is given such that each node contains an additional random pointer that could point to any node in the
list or null.
Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


"""
O(n) runtime, O(1) space – Modify original structure

If we modify the next node of the original node to point to its own copy, we can assign the random node pointers of each 
copy easily with the following code: node.next.random = node.random.next
"""
class Solution:
    def copy_random_list(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Create a copy of each of the original node and insert them in between two original nodes in an alternate fashion
        p = head
        while p:
            next = p.next
            copy = RandomListNode(p.label)
            p.next = copy
            copy.next = next
            p = next

        # Assign random pointer of each node copy
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next

        # Restore the input to its original configuration
        p = head
        headCopy = p.next if p else None
        while p:
            copy = p.next
            p.next = copy.next
            p = p.next
            copy.next = p.next if p else None
        return headCopy

if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.random = head.next
    result = Solution().copy_random_list(head)
    print result.label
    print result.next.label
    print result.random.label
