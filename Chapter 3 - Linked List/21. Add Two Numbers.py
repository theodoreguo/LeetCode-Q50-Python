# coding=utf-8
"""
Question:
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of
their nodes contains a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n) runtime, O(1) space – Simple one-pass
class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            digit = carry + x + y
            carry = digit / 10
            current.next = ListNode(digit % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().add_two_numbers(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)

    c, c.next = ListNode(9), ListNode(9)
    d = ListNode(1)
    result = Solution().add_two_numbers(c, d)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)
