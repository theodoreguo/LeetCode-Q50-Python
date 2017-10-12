# coding=utf-8
"""
Question:
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1 -> 2 -> 3 -> 4, you should return the list as 2 -> 1 -> 4 -> 3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Example Questions Candidate Might Ask:
Q: What if the number of nodes in the linked list has only odd number of nodes?
A: The last node should not be swapped.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

"""
O(n) runtime, O(1) space

Let’s assume p, q, r are the current, next, and next’s next node.
We could swap the nodes pairwise by adjusting where it’s pointing next: 
q.next = p
p.next = r
The above operations transform the list from {p -> q -> r -> s} to {q -> p -> r -> s}. 
If the next pair of nodes exists, we should remember to connect p’s next to s. 
Therefore, we should record the current node before advancing to the next pair of nodes.
 
To determine the new list’s head, you look at if the list contains two or more elements. Basically, these extra conditional 
statements could be avoided by inserting an extra node (also known as the dummy head) to the front of the list.
"""
class Solution(object):
    def swap_pairs(self, head):
        """
        :type head: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = head
        prev = dummy
        while p and p.next:
            q, r = p.next, p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummy.next

class Solution2:
    def swap_pairs(self, head):
        """
        :type head: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one
        return dummy.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next = ListNode(2), ListNode(3), ListNode(4)
    print Solution().swap_pairs(head)

    head2 = ListNode(1)
    head2.next, head2.next.next, head2.next.next.next = ListNode(2), ListNode(3), ListNode(4)
    print Solution2().swap_pairs(head2)
