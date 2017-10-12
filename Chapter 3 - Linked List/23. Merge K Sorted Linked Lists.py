# coding=utf-8
"""
Question:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

# O(nk log k) runtime, O(1) space – Divide and conquer using two way merge
class Solution(object):
    def merge_k_lists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge_two_lists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1
        while right > 0:
            left = 0
            while left < right:
                lists[left] = merge_two_lists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]

# O(nk log k) runtime, O(1) space – Divide and conquer using two way merge
class Solution2:
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    def merge_k_lists(self, lists):
        def merge_two_lists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def merge_k_lists_helper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]
            return merge_two_lists(merge_k_lists_helper(lists, begin, (begin + end) / 2),
                                   merge_k_lists_helper(lists, (begin + end) / 2 + 1, end))

        return merge_k_lists_helper(lists, 0, len(lists) - 1)

# O(nk log k) runtime, O(k) space – Heap
import heapq

class Solution3:
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    def merge_k_lists(self, lists):
        dummy = ListNode(0)
        current = dummy

        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))

        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next

if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list2 = ListNode(2)
    list2.next = ListNode(4)

    print Solution().merge_k_lists([list1, list2])
    # print Solution2().merge_k_lists([list1, list2])
    # print Solution3().merge_k_lists([list1, list2])
